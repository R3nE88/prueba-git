from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def Hola(request):
    return HttpResponse("<h2> un ejemplo en git 2 </h2>")