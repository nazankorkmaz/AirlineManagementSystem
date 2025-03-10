from django.shortcuts import render
from django.http import HttpResponse

from airplane.models import Airplane
from airplane.serializer import AirplaneSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def deneme(requests):
    return HttpResponse("deneme yüklendi mi")

@api_view(['GET'])
def airplane_list(request):
    airplanes = Airplane.objects.all()
    serializer = AirplaneSerializer(airplanes, many = True)
    return Response(serializer.data)