from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.deneme3,name="deneme3" ),
]
