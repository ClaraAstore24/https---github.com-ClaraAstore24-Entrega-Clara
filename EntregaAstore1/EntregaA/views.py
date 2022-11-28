from django.shortcuts import render
from django.http import HttpResponse
from EntregaA.models import Registrar, Usuario


# Create your views here.


def inicio(request):
    return render(request, "EntregaA/inicio.html")

def ingresar_usuario(request):
    return render(request, "EntregaA/usuario.html")

def vista_registro(request):
    if request.method == "POST":
        Nombre_Persona = request.POST["nombre"]
        Nombre_Contraseña = request.POST["contraseña"]
        Nombre_Email = request.POST["email"]

        register = Registrar(nombre=Nombre_Persona, contraseña=Nombre_Contraseña, email=Nombre_Email)
        register.save()
        
    return render(request, "EntregaA/registro_formulario.html")


def vista_comprar_boletos(request):
    return render(request, "EntregaA/comprarboletos.html")

def vista_sobre_nosotros(request):
    return render(request, "EntregaA/sobreNosotros.html")

#def Vista_plantilla(request):
   # listado = Usuario.objects.all()
   # Vista = ""
   # for USUARIO in listado:
    #    Vista += Usuario.nombre + " | "

  #  return HttpResponse