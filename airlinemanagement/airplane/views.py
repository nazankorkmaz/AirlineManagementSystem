from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deneme(requests):
    return HttpResponse("deneme yüklendi mi")