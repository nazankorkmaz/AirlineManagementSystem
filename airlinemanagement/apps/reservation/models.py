from django.db import models

# Create your models here.

from django.utils.crypto import get_random_string

from apps.flight.models import Flight

class Reservation(models.Model):
    passenger_name = models.CharField(max_length=100)

    passenger_email = models.EmailField()

    reservation_code = models.CharField(max_length=6,unique=True,blank=True) 

    flight = models.ForeignKey(Flight,on_delete= models.CASCADE, related_name='reservation_flight') # her reservasyon bir ucusa ait olmali | bir ucusun birden fazla rezervasyonu olabilir

    status = models.BooleanField(default=True)
    #rezervasyon durumu

    created_at = models.DateTimeField(auto_now_add=True)
    # rezerveasyon olusturulma tarihi

    def make_reservation_code(self):

        return get_random_string(length=6, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    def save(self, *args, **kwargs):
        if not self.reservation_code:
            while True:
                code = self.make_reservation_code()
                if not Reservation.objects.filter(reservation_code = code).exists():
                    self.reservation_code = code
                    break
        super().save(*args, **kwargs)