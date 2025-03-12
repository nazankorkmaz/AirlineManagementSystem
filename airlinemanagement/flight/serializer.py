from datetime import timedelta
from rest_framework import serializers
from flight.models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


    def validate(self, data):
        airplane = data.get('airplane')
        departure_time = data.get('departure_time')
        arrival_time = data.get('arrival_time')

        # Ayni ucagin ucuslari alinir
        overlapping_flights = Flight.objects.filter(
            airplane=airplane,
            departure_time__lt=arrival_time,
            arrival_time__gt=departure_time
        )

        # Ayni zamanda var mi kontrolu yapilir
        if overlapping_flights.exists():
            raise serializers.ValidationError("This airplane already has a flight scheduled during this time.")

        # 1 saat ileri ve geri kontrolleri yapilir
        one_hour_before = departure_time - timedelta(hours=1)
        one_hour_after = arrival_time + timedelta(hours=1)

        close_flights = Flight.objects.filter(
            airplane=airplane,
            departure_time__range=(one_hour_before, one_hour_after)
        )

        if close_flights.exists():
            raise serializers.ValidationError("There must be at least 1 hour between two flights of the same airplane.")

        return data
