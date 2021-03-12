from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def Hola(request):
    return HttpResponse("<h3> un ejemplo en git 3, desde la otra computadora </h3>")