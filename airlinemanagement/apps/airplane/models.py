from django.db import models
import random

# Create your models here.

class Airplane(models.Model):
    tail_number = models.CharField(max_length=50, unique=True) #kuyruk numarasi - benzersiz 

    model = models.CharField(max_length=50)

    capacity = models.IntegerField()

    production_year = models.IntegerField()

    status = models.BooleanField(default=True)



