from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from apps.reservation.models import Reservation
from apps.reservation.serializer import ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def reservation(request):

    if request.method == "GET":
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    
    elif  request.method == "POST":
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PATCH','DELETE'])
def reservation_id(request,id):
    try:
        reservations = Reservation.objects.get(pk=id)
        
    except Reservation.DoesNotExist:
        return Response({"error":"Reservation not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ReservationSerializer(reservations)
        return Response(serializer.data)
    
    if request.method == "PATCH":
        serializer = ReservationSerializer(reservations, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        reservations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     
