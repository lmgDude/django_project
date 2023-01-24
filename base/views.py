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
    return render(request, )


def code_404(request, exception):
    response = render(request, 'base/code404.html')
    response.status_code = 404
    return response

