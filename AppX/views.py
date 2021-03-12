from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def Hola(request):
    return HttpResponse("<h1> ejemplo en git </h1>")