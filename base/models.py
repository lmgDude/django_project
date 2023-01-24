from django.db import models


class Profession(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название профессии')
    description = models.TextField(blank=True, verbose_name='Описание')
    images = models.ImageField(upload_to='photo_prof/', verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"
        ordering = ['name']
        db_table = 'profession'


class Vacancies(models.Model):
    name = models.TextField(verbose_name='Название вакансии')
    skills = models.TextField(blank=True, null=True, verbose_name='Навыки')
    salary_from = models.IntegerField(blank=True, null=True, verbose_name='З/п от')
    salary_to = models.IntegerField(blank=True, null=True, verbose_name='З/п до')
    currency = models.TextField(blank=True, null=True, verbose_name='Валюта')
    town = models.TextField(blank=True, null=True, verbose_name='Город')
    datetime = models.TextField(blank=True, null=True, verbose_name='Дата и время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        db_table = 'vacancies'


class Demand(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    file_csv = models.FileField(upload_to='demand_csv/', verbose_name='Файл csv')
    file_png = models.ImageField(upload_to='demand_png/', verbose_name='Файл png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Востребованность"
        verbose_name_plural = "Востребованности"


class Geography(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    file_csv = models.FileField(upload_to='demand_csv/', verbose_name='Файл csv')
    file_png = models.ImageField(upload_to='demand_png/', verbose_name='Файл png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "География"
        verbose_name_plural = "Географии"
        db_table = 'geography'


class Skills(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    file_csv = models.FileField(upload_to='demand_csv/', verbose_name='Файл csv')
    file_png = models.ImageField(upload_to='demand_png/', verbose_name='Файл png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Нывыки"
        db_table = 'skills'
