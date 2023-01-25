from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("demand/", views.demand, name="demand"),
    path("geography/", views.geography, name="geography"),
    path("skills/", views.skills, name="skills"),
    path("last_vacancies/", views.last_vacancies, name="last_vacancies"),
    path("mario/", views.fake_code_404, name="mario")
]
