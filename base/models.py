from django.db import models


# Create your models here.
class Profession(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to='photo_prof/')

