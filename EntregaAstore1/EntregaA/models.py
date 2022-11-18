from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()

class Voletos_avion(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    
class Viajes_disponibles(models.Model):
    destino = models.CharField(max_length = 50)
    horario= models.IntegerField()