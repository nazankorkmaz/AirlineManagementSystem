from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    #path('',views.deneme2,name="deneme2" ),
    path('',views.flight_list),

]
