from django.urls import path 
from EntregaA.views import *


urlpatterns = [
    path("", inicio, name="Inicio"),
    path("usuario/", ingresar_usuario, name="Usuario"),
    path("boletosavion/", vista_comprar_boletos, name="Boletos"),
    path("sobrenosotros/", vista_sobre_nosotros, name="SobreNosotros"),
    path("registro/", vista_registro, name= "Registro"),
]