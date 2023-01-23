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
    return render(request, )


def skills(request):
    """data_frame_skills = pd.DataFrame(columns=['skills', 'date'])
    vacancies_list = list(Vacancies.objects.all())
    vacancies_count = len(vacancies_list)

    for vacancy in vacancies_list:
        year = vacancy.datetime[:4]
        if vacancy.skills != '':
            data_frame_skills.loc[len(data_frame_skills.index)] = {'skills': vacancy.skills, 'date': year}"""

    return render(request, )


def last_vacancies(request):
    return render(request, )


def code_404(request, exception):
    response = render(request, 'base/code404.html')
    response.status_code = 404
    return response

