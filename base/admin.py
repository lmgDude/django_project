from django.contrib import admin
from .models import Profession, Vacancies, Demand, Geography


# Register your models here.
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'images')
    search_fields = ('name', )


class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary_to', 'currency', 'town')
    search_fields = ('name', )


class DemandAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_csv')
    search_fields = ('name', 'file_csv')


class GeographyAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_csv')
    search_fields = ('name', 'file_csv')


admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Vacancies, VacanciesAdmin)
admin.site.register(Demand, DemandAdmin)
admin.site.register(Geography, GeographyAdmin)


