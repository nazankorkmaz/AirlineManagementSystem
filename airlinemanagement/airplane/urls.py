from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    #path('',views.deneme,name="deneme" ),
    path('',views.airplane_list),
    path('<int:id>',views.airplane_id),
    path('create/',views.airplanes_create),
    path('update/<int:id>',views.airplane_patch),
    path('delete/<int:id>',views.airplane_delete),
    path('<int:id>/flights',views.airplane_flights),
]
