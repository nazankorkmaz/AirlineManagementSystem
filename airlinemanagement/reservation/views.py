from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from reservation.models import Reservation
from reservation.serializer import ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def deneme3(requests):
    return HttpResponse("deneme3 yüklendi mi")


@api_view(['GET'])
def reservation_list(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)