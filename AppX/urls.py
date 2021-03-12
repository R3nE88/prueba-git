from django.urls import path
from .views import Hola 

urlpatterns = [
    path('hola/', Hola),
]
