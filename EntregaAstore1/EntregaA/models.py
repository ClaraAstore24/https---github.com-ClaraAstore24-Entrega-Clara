from django.db import models

# Create your models here.

class ingresar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()

class comprar_voletos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    
class sobre_nosotros(models.Model):
    destino = models.CharField(max_length = 50)
    horario= models.IntegerField()