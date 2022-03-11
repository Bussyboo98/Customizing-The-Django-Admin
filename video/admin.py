from ast import mod
from dataclasses import field
from re import search
from django.contrib import admin
from . import models
# Register your models here.

class MovieAdmin(admin.ModelAdmin):

    fields = ['release_year','title','length']
    search_fields = ['title']
    list_filter = ['release_year','title','length']
    list_display = ['title','release_year','length']
    list_editable = ['release_year','length']

admin.site.register(models.Customers)
admin.site.register(models.Movie, MovieAdmin)