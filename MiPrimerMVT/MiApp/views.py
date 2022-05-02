from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar
# Create your views here.

def familiar(self):
    familiar=Familiar(nombre="Agustin", apellido="Buisan", edad=25, mail="agustin.buisan@gmail.com", rol_familiar="Hijo")
    familiar.save()
    show_familiar = f"Mi nombre es: {familiar.nombre} y soy {familiar.rol_familiar}"

    return HttpResponse(show_familiar)
    
