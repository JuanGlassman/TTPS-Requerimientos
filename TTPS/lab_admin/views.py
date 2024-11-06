from django.shortcuts import render, get_object_or_404
from estudios.models import Estudio, EstadoEstudio
from estudios import views as estudio_estado

def estudios(request):
    estudios = Estudio.objects.order_by("fecha")
    return render(request, "estudios.html", { "estudios": estudios, "estados": EstadoEstudio })

def pagar_admin(request, estudio_id):
    estudio = get_object_or_404(Estudio, id_estudio=estudio_id)
    res, estudio = estudio_estado.estudio_pagado(estudio)
    estudio.save()    
    return render(request, "estudio.html", {'estudio': estudio})