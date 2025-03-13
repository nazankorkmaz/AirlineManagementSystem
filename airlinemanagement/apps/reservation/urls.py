from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.reservation),
    path('<int:id>',views.reservation_id),

]
