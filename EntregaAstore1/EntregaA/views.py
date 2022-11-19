from django.shortcuts import render
from django.http import HttpResponse
from EntregaA.models import Usuario


# Create your views here.



def inicio(request):
    return HttpResponse("Estas en el inicio")

def usuarios(request):
    return HttpResponse("Crear usuario")

def voletos_avion(request):
    return HttpResponse("Estas en voletos de avion")

def viajes_disponibles(request):
    return HttpResponse("Estas en viajes disponibles")


#def Vista_plantilla(request):
   # listado = Usuario.objects.all()
   # Vista = ""
   # for USUARIO in listado:
    #    Vista += Usuario.nombre + " | "

  #  return HttpResponse