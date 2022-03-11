from operator import length_hint, mod
from django.db import models
from django.forms import CharField

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=256)
    length = models.PositiveBigIntegerField()
    release_year = models.PositiveBigIntegerField()
    def __str__(self):
        return self.title

class Customers(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveBigIntegerField()

    def __str__(self):
        return self.first_name
        from operator import length_hint, mod
from django.db import models
from django.forms import CharField

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=256)
    length = models.PositiveBigIntegerField()
    release_year = models.PositiveBigIntegerField()
    def __str__(self):
        return self.title

class Customers(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveBigIntegerField()

    def __str__(self):
        return self.first_name