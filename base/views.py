from django.shortcuts import render
from .models import *


def main(request):
    main_info = {'name': Profession.objects.last()}
    return render(request, 'base/main.html', context=main_info)


def demand(request):
    return render(request, 'base/demand.html')


def geography(request):
    return render(request, )


def skills(request):
    return render(request, )


def last_vacancies(request):
    return render(request, )


def code_404(request, exception):
    response = render(request, 'base/code404.html')
    response.status_code = 404
    return response

