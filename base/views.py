from django.shortcuts import render


def main(request):
    return render(request)


def demand(request):
    return render(request, "projects.html")


def geography(request):
    return render(request, "contact.html")


def skills(request):
    return render(request, "contact.html")


def last_vacancies(request):
    return render(request, "contact.html")
