from rest_framework import serializers
from apps.reservation.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    
    def validate(self, data):  # data sozluk yapısında geliyor 
        flight = data['flight']  #ilgili ucus  # bunu yazdırırsan Flight modelindeki str methodu gelir yoksa ham hali gelir
        current_reservations = Reservation.objects.filter(flight=flight).count()  #ucusa yapilan rezervasyon sayisi

        #flight Foreign key oldugu icin dogrudan flight nesnesidir

        """
        flight bir Flight model nesnesidir.
        flight.airplane, bu uçuşa atanmış Airplane nesnesine erişir.
        flight.airplane.capacity, bu uçağın kapasitesini (IntegerField) döndürür.
        """
        if current_reservations >= flight.airplane.capacity:
            raise serializers.ValidationError("This flight is fully booked. No more seats available.")
        
        return data
    
    def validate_passenger_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Passenger name must be at least 5 characters long.")
        return value