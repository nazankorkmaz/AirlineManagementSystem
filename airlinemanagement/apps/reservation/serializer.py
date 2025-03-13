from rest_framework import serializers
from apps.reservation.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    
    def validate(self, data):
        flight = data['flight']
        current_reservations = Reservation.objects.filter(flight=flight).count()

        if current_reservations >= flight.airplane.capacity:
            raise serializers.ValidationError("This flight is fully booked. No more seats available.")
        
        return data