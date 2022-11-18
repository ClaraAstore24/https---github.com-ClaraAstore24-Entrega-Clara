from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from EntregaA.models import Usuario

def Vista_usuario(request):
    listado = Usuario.objects.all()
    Vista = ""
    for USUARIO in listado:
        Vista += Usuario.nombre + " | "

    return HttpResponse