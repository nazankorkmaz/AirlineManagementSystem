from django.shortcuts import render
from django.http import HttpResponse

from airplane.models import Airplane
from airplane.serializer import AirplaneSerializer
from flight.serializer import FlightSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def deneme(requests):
    return HttpResponse("deneme yüklendi mi")

@api_view(['GET'])
def airplane_list(request):
    airplanes = Airplane.objects.all()
    serializer = AirplaneSerializer(airplanes, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def airplane_id(request,id):
    try:
        airplanes = Airplane.objects.get(pk=id)
        serializer = AirplaneSerializer(airplanes)
        return Response(serializer.data)
    except Airplane.DoesNotExist:
        return Response({"error":"Airplane not found"},status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def airplanes_create(request):
    serializer = AirplaneSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'PUT'])
def airplane_patch(request,id):
    try:
        airplane = Airplane.objects.get(pk=id)
        serializer = AirplaneSerializer(airplane, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Airplane.DoesNotExist:
        return Response({"error": "Airplane not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def airplane_delete(request,id):
    try:
        airplane = Airplane.objects.get(pk=id)
        airplane.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Airplane.DoesNotExist:
        return Response({"error": "Airplane not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def airplane_flights(request, id):
    try:
        airplane = Airplane.objects.get(pk=id)
        flights = airplane.flights.all()  # related_name ile bağlı uçuşları çekiyoruz
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
    except Airplane.DoesNotExist:
        return Response({"error": "Airplane not found"}, status=status.HTTP_404_NOT_FOUND)
