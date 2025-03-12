from django.shortcuts import render
from django.http import HttpResponse

from airplane.models import Airplane
from airplane.serializer import AirplaneSerializer
from flight.serializer import FlightSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def airplane(request):
    if request.method == "GET":
        airplanes = Airplane.objects.all()
        serializer = AirplaneSerializer(airplanes, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AirplaneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH','DELETE'])
def airplane_id(request,id):
    try:
        airplanes = Airplane.objects.get(pk=id)
        
    except Airplane.DoesNotExist:
        return Response({"error":"Airplane not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AirplaneSerializer(airplanes)
        return Response(serializer.data)
    
    if request.method == "PATCH":
        serializer = AirplaneSerializer(airplanes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        airplanes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     


@api_view(['GET'])
def airplane_flights(request, id):
    try:
        airplane = Airplane.objects.get(pk=id)
        flights = airplane.flights.all()  # related_name ile bağlı uçuşları çekiyoruz
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
    except Airplane.DoesNotExist:
        return Response({"error": "Airplane not found"}, status=status.HTTP_404_NOT_FOUND)

