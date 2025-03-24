from rest_framework import serializers
from apps.airplane.models import Airplane
import re

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane  #airplane modeline bagli
        fields = '__all__' #modeldeki tum alanlari Jsona cevir

    #ozel validasyon
    def validate_tail_number(self, value):
        if not re.match(r'^[A-Z]{2}-[A-Z0-9]{3}$', value):
            raise serializers.ValidationError("Tail number must be in the format AB-C5D (two uppercase letters, a dash, and three uppercase letters or digits).")
        return value
    
#serializers.ModelSerializer, Django Rest Framework (DRF) tarafından sağlanan bir sınıftır. Bir modeli temel alarak otomatik olarak serializer oluşturur, yani:

#Modeldeki tüm alanları otomatik olarak JSON formatına çevirir.

"""
sadece belirli alanlari isteseydik boyle olurdu all yerine
fields = ['id', 'name', 'tail_number']
"""

"""
Django Rest Framework’te (DRF) bir field-specific validation (alan bazlı doğrulama) yaparken, validate_<field_name> şeklinde bir metot yazarsak, DRF bunu otomatik olarak o alanın doğrulama fonksiyonu olarak kabul eder.
"""