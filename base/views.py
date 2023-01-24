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
        'geography_salary_csv': pd.read_csv(Geography.objects.get(name='geography_salary').file_csv).to_html(index=False),
        'geography_salary_png': Geography.objects.get(name='geography_salary').file_png,
        'geography_vacancy_csv': pd.read_csv(Geography.objects.get(name='geography_vacancy').file_csv).to_html(index=False),
        'geography_vacancy_png': Geography.objects.get(name='geography_vacancy').file_png,
    }
    return render(request, 'base/geograpy.html', context=geography_info)


def skills(request):


    return render(request, )


def last_vacancies(request):
    return render(request, )


def code_404(request, exception):
    response = render(request, 'base/code404.html')
    response.status_code = 404
    return response

