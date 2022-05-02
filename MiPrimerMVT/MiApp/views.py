from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar
# Create your views here.

def familiar(self):
    familiar=Familiar(nombre="Fernando", apellido="Buisan", edad=62, mail="fernandoxxx@gmail.com", rol_familiar="Padre")
    familiar.save()
    show_familiar = f"Mi nombre es: {familiar.nombre} y soy {familiar.rol_familiar}"

    return HttpResponse(show_familiar)
    
