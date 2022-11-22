from django.shortcuts import render
from django.http import HttpResponse
from EntregaA.models import *


# Create your views here.


def inicio(request):
    return render(request, "EntregaA/inicio.html")

def ingresar_usuario(request):
    return render(request, "EntregaA/usuario.html")

def vista_comprar_voletos(request):
    return render(request, "EntregaA/comprarVoletos.html")

def vista_sobre_nosotros(request):
    return render(request, "EntregaA/sobreNosotros.html")

#def Vista_plantilla(request):
   # listado = Usuario.objects.all()
   # Vista = ""
   # for USUARIO in listado:
    #    Vista += Usuario.nombre + " | "

  #  return HttpResponse