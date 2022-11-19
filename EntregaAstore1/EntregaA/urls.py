from django.urls import path, include
from EntregaA.views import *

urlpatterns = [
    path("usuario/", usuario),
    path("voletos_avion/", voletos_avion),
    path("viajes_disponibles/", viajes_disponibles),

    path("EntregaA/", include("EntregaA.urls"))

]