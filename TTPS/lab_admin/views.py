from django.shortcuts import render
from estudios.models import Estudio, EstadoEstudio

def estudios(request):
    estudios = Estudio.objects.order_by("fecha")
    return render(request, "estudios.html", { "estudios": estudios, "estados": EstadoEstudio })
