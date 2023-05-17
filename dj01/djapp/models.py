from django.db import models

# Create your models here.

class Students_models1(models.Model):
    name1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
    gender = models.CharField(max_length=6, null=True)

class Courses(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    type_of_cource = models.CharField(max_length=100)
