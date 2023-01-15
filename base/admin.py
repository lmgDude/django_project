from django.contrib import admin
from .models import Profession


# Register your models here.
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'images')
    search_fields = ('name', )


admin.site.register(Profession, ProfessionAdmin)
