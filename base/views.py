from django.shortcuts import render


def main(request):
    return render(request, )


def demand(request):
    return render(request, )


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

