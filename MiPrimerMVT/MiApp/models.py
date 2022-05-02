from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    edad= models.IntegerField()
    mail=models.EmailField()
    rol_familiar= models.CharField(max_length=20)