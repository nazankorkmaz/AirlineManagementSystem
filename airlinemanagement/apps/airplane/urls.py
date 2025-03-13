from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [

    path('',views.airplane),
    path('<int:id>',views.airplane_id),
    path('<int:id>/flights',views.airplane_flights), # Ucaga ait ucuslar alinir
]
