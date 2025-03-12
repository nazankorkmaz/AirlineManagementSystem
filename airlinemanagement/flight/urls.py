from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.flight),
    path('<int:id>',views.flight_id),
    path('<int:id>/reservations',views.flight_reservation), # ucusa ait rezervasyonlar alinir
]
