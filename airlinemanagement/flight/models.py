from django.db import models

from airplane.models import Airplane

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length=50, unique=True)
    # ucus numarasi - benzersiz

    departure = models.CharField(max_length=100)
    #kalkis havaalani

    destination = models.CharField(max_length=100)
    # inis havaalani

    departure_time = models.DateTimeField() #kalkis zamani

    arrival_time = models.DateTimeField() # varis zamani

    airplane = models.ForeignKey(Airplane,on_delete=models.CASCADE, related_name='flights_airplane') # her ucus bir ucaga atanir - ucaga birden fazşa ucus atanabilir