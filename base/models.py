from django.db import models


# Create your models here.
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
