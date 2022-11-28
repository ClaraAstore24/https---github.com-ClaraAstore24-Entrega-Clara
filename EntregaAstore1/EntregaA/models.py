from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.IntegerField()
    email = models.EmailField()

class Registrar(models.Model):
    nombre = models.CharField(max_length=50)
    contraseña = models.IntegerField()
    email = models.EmailField()

class Comprar_boletos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    
class Nosotros(models.Model):
    informacion = models.CharField(max_length=100)
    fecha = models.IntegerField()


