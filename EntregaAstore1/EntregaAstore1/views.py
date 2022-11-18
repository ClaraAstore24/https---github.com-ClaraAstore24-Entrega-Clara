from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

# Create your views here.

def vista_plantilla(request):
    archivo = open(r'C:\Users\matia\OneDrive\Documentos\Coder\EntregaAstore\EntregaAstore1\EntregaAstore1\templates\entrega.html')


def fecha_actual(request):
    hoy=datetime.now().strftime("%d|%m|%Y")
    return HttpResponse(f"Fecha actual: {hoy}")