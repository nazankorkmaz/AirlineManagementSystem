from datetime import timedelta  #zaman araliklarini hesaplamak icin
from rest_framework import serializers
from apps.flight.models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


    #tum ucus verilerini bir butun olarak dogrular.
    def validate(self, data):
        airplane = data.get('airplane')  #kullanıcının gonderdigi verinin json dictine donusturulmus halini alir yani
        departure_time = data.get('departure_time')
        arrival_time = data.get('arrival_time')

        # Ayni ucagin ucuslari alinir
        overlapping_flights = Flight.objects.filter(
            airplane=airplane,
            departure_time__lt=arrival_time, #kalkis saati inis saatinden  kucukse
            arrival_time__gt=departure_time # inis saati kalkis saatinden buyukse 
        )

        # Ayni zamanda var mi kontrolu yapilir
        if overlapping_flights.exists():
            raise serializers.ValidationError("This airplane already has a flight scheduled during this time.")

        # 1 saat ileri ve geri kontrolleri yapilir
        one_hour_before = departure_time - timedelta(hours=1)
        one_hour_after = arrival_time + timedelta(hours=1)

        #bir saat once ve sonra ucus var mi
        close_flights = Flight.objects.filter(
            airplane=airplane,
            departure_time__range=(one_hour_before, one_hour_after)  #cunku onemliolan yeni ucusun baslangic saati
        )

        #departure_time__range=(x, y), Django ORM’de bir tarih-saat alanının belirli bir aralık içinde olup olmadığını kontrol eden filtredir.

        #2.yol
        """
        Q() nesnesi ve gte (büyük eşit) ile lte (küçük eşit) operatörleri
        
        close_flights = Flight.objects.filter(
            airplane=airplane
        ).filter(
            Q(departure_time__gte=one_hour_before) & Q(departure_time__lte=one_hour_after)
        )
        """

        if close_flights.exists():
            raise serializers.ValidationError("There must be at least 1 hour between two flights of the same airplane.")

        return data # ucus kaydi yapilir yani
