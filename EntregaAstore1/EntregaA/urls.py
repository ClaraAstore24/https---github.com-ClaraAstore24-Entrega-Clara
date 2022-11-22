from django.urls import path 
from EntregaA.views import *


urlpatterns = [
    path("", inicio, name="Inicio"),
    path("usuario/", ingresar_usuario, name="Usuario"),
    path("voletosavion/", vista_comprar_voletos, name="Voletos"),
    path("sobrenosotros/", vista_sobre_nosotros, name="Sobre-Nosotros"),
]