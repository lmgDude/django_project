import datetime
import requests
from django.shortcuts import render
from .models import *
import pandas as pd


def main(request):
    main_info = {'name': Profession.objects.last()}
    return render(request, 'base/main.html', context=main_info)


def demand(request):
    demand_info = {
        'salary_all_csv': pd.read_csv(Demand.objects.get(name='salary_all').file_csv).to_html(index=False),
        'salary_all_png': Demand.objects.get(name='salary_all').file_png,
        'vacancy_all_csv': pd.read_csv(Demand.objects.get(name='vacancy_all').file_csv).to_html(index=False),
        'vacancy_all_png': Demand.objects.get(name='vacancy_all').file_png,
        'salary_csv': pd.read_csv(Demand.objects.get(name='salary').file_csv).to_html(index=False),
        'salary_png': Demand.objects.get(name='salary').file_png,
        'vacancy_csv': pd.read_csv(Demand.objects.get(name='vacancy').file_csv).to_html(index=False),
        'vacancy_png': Demand.objects.get(name='vacancy').file_png,
    }
    return render(request, 'base/demand.html', context=demand_info)


def geography(request):
    geography_info = {
        'geography_salary_csv': pd.read_csv(Geography.objects.get(name='geography_salary').file_csv).to_html(
            index=False),
        'geography_salary_png': Geography.objects.get(name='geography_salary').file_png,
        'geography_vacancy_csv': pd.read_csv(Geography.objects.get(name='geography_vacancy').file_csv).to_html(
            index=False),
        'geography_vacancy_png': Geography.objects.get(name='geography_vacancy').file_png,
    }
    return render(request, 'base/geograpy.html', context=geography_info)


def skills(request):
    skills_info = {
        '2015_csv': pd.read_csv(Skills.objects.get(name='2015').file_csv).to_html(
            index=False),
        '2015_png': Skills.objects.get(name='2015').file_png,
        '2016_csv': pd.read_csv(Skills.objects.get(name='2016').file_csv).to_html(
            index=False),
        '2016_png': Skills.objects.get(name='2016').file_png,
        '2017_csv': pd.read_csv(Skills.objects.get(name='2017').file_csv).to_html(
            index=False),
        '2017_png': Skills.objects.get(name='2017').file_png,
        '2018_csv': pd.read_csv(Skills.objects.get(name='2018').file_csv).to_html(
            index=False),
        '2018_png': Skills.objects.get(name='2018').file_png,
        '2019_csv': pd.read_csv(Skills.objects.get(name='2019').file_csv).to_html(
            index=False),
        '2019_png': Skills.objects.get(name='2019').file_png,
        '2020_csv': pd.read_csv(Skills.objects.get(name='2020').file_csv).to_html(
            index=False),
        '2020_png': Skills.objects.get(name='2020').file_png,
        '2021_csv': pd.read_csv(Skills.objects.get(name='2021').file_csv).to_html(
            index=False),
        '2021_png': Skills.objects.get(name='2021').file_png,
        '2022_csv': pd.read_csv(Skills.objects.get(name='2022').file_csv).to_html(
            index=False),
        '2022_png': Skills.objects.get(name='2022').file_png
    }

    return render(request, 'base/skills.html', context=skills_info)


def last_vacancies(request):
    def get_vacancies_on_page(date, page, result):
        path = f'https://api.hh.ru/vacancies?specialization=1&date_from={date}&date_to={date}&page={page}&per_page=100'
        [result.append([element['name'],
                        element['snippet']['responsibility'],
                        element['snippet']['requirement'],
                        element['employer']['name'],
                        element['salary']['from'] if element['salary'] is not None else None,
                        element['salary']['to'] if element['salary'] is not None else None,
                        element['salary']['currency'] if element['salary'] is not None else None,
                        element['area']['name'],
                        element['published_at']]) for element in requests.get(path).json()['items']]

    def get_average(element):
        salary = list(map(float, list(filter(None, [element.salary_from, element.salary_to]))))
        summary = int(sum(salary) / len(salary)) if len(salary) > 0 else None
        return f'{summary} {element.salary_currency}' if summary is not None else None

    def create_data_file(date):
        result = []
        pages = 15
        [get_vacancies_on_page(date, page, result) for page in range(pages)]

        header = ["name", "description", "key_skills", "employer_name", "salary_from", "salary_to", "salary_currency",
                  "area_name", "published_at"]
        rus_header = ["Название вакансии", "Описание вакансии", "Навыки", "Компания", "Оклад",
                      "Название региона", "Дата публикации вакансии"]

        data_frame = pd.DataFrame(result, columns=header).fillna("")
        data_frame = data_frame[
            data_frame.name.str.lower().str.contains("защита")
            | data_frame.name.str.lower().str.contains("информационной")
            | data_frame.name.str.lower().str.contains("информационная")
            | data_frame.name.str.lower().str.contains("information security specialist")
            | data_frame.name.str.lower().str.contains("information security")
            | data_frame.name.str.lower().str.contains("фахівець служби безпеки")
            | data_frame.name.str.lower().str.contains("cyber security")
            ]
        data_frame.insert(4, 'salary', data_frame.apply(lambda element: get_average(element), axis=1))
        data_frame = data_frame.drop(columns=['salary_from', 'salary_to', 'salary_currency']).fillna("").sort_values(
            by=['published_at'], ascending=False)[
                     :10]
        data_frame.published_at = data_frame.published_at.apply(lambda x: x[:-5])
        data_frame.columns = rus_header
        return data_frame

    last_vacancies_info = {
        'last_vacancies_csv': create_data_file(str(datetime.datetime.now().date())[:-1]
                                               + str(int(str(datetime.datetime.now().date())[-1]) - 1)
                                               if int(str(datetime.datetime.now().date())[-1]) - 1 != 0
                                               else "1").to_html(index=False)
    }

    return render(request, 'base/last_vacancies.html', context=last_vacancies_info)


def fake_code_404(request):
    return render(request, 'base/code404.html')


def code_404(request, exception):
    response = render(request, 'base/code404.html')
    response.status_code = 404
    return response
