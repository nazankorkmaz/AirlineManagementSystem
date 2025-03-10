from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from flight.models import Flight
from flight.serializer import FlightSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def deneme2(requests):
    return HttpResponse("deneme2 yüklendi mi")

# Flight Endpoints
@api_view(['GET'])
def flight_list(request):
    flights = Flight.objects.all()
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)