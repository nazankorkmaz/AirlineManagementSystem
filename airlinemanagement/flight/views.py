from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from flight.models import Flight
from flight.serializer import FlightSerializer
from reservation.models import Reservation
from reservation.serializer import ReservationSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Flight Endpoints
@api_view(['GET','POST'])
def flight(request):
    if request.method == "GET":
        flights = Flight.objects.all()

        # filtreleme alinsin mi kontrolleri yapilir
        departure_location = request.GET.get('departure')
        destination_location = request.GET.get('destination')
        departure_date = request.GET.get('departure_time')
        arrival_date = request.GET.get('arrival_time')

        if departure_location:
            flights = flights.filter(departure__icontains=departure_location)
        if destination_location:
            flights = flights.filter(destination__icontains=destination_location)
        if departure_date:
            flights = flights.filter(departure_time__date=departure_date)
        if arrival_date:
            flights = flights.filter(arrival_time__date=arrival_date)

        
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
@api_view(['GET','PATCH','DELETE'])
def flight_id(request,id):
    try:
        flights = Flight.objects.get(pk=id)
        
    except Flight.DoesNotExist:
        return Response({"error":"Flight not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = FlightSerializer(flights)
        return Response(serializer.data)
    
    if request.method == "PATCH":
        serializer = FlightSerializer(flights, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        flights.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     

# bir ucusun tum rezervasyonlarini al.
@api_view(['GET'])
def flight_reservation(request,id):
    try:
        # Flight modelinden belirli bir uçuş alınıyor
        flight = Flight.objects.get(pk=id)
    except Flight.DoesNotExist:
        return Response({"error": "Flight not found"}, status=status.HTTP_404_NOT_FOUND)

    # Flighttaki tum rezervasyonlar alinir
    reservations = Reservation.objects.filter(flight=flight)  # ForeignKey ters iliskisi kurulur
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

