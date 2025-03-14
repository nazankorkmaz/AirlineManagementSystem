from rest_framework import serializers
from apps.airplane.models import Airplane
import re

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'

    def validate_tail_number(self, value):
        if not re.match(r'^[A-Z]{2}-[A-Z0-9]{3}$', value):
            raise serializers.ValidationError("Tail number must be in the format AB-C5D (two uppercase letters, a dash, and three uppercase letters or digits).")
        return value