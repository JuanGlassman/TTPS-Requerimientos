from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from estudios.models import Estudio, EstadoEstudio

def estudio_terminado(estudio):
    return estudio.estado in [EstadoEstudio.CANCELADO, EstadoEstudio.FINALIZADO]

def estudio_presupuestado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.INICIADO):
        estudio.estado = EstadoEstudio.PRESUPUESTADO
    return True, estudio

def estudio_pagado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.PRESUPUESTADO):
        estudio.estado = EstadoEstudio.PAGADO
        return True, estudio
    else:
        return False, estudio

def estudio_autorizado(estudio):
    if estudio_terminado(estudio):
        return False, estudio

    if (estudio.estado == EstadoEstudio.PAGADO):
        estudio.estado = EstadoEstudio.AUTORIZADO
        return True, estudio
    else:
        return False, estudio

def estudio_confirmado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.AUTORIZADO):
        estudio.estado = EstadoEstudio.TURNO_CONFIRMADO
        return True, estudio
    else:
        return False, estudio

def estudio_realizado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.TURNO_CONFIRMADO):
        estudio.estado = EstadoEstudio.REALIZADA
        return True, estudio
    else:
        return False, estudio

def estudio_centralizado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.REALIZADA):
        estudio.estado = EstadoEstudio.CENTRALIZADA
        return True, estudio
    else:
        return False, estudio

def estudio_enviado_exterior(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.CENTRALIZADA):
        estudio.estado = EstadoEstudio.ENVIADA_EXTERIOR
        return True, estudio
    else:
        return False, estudio
    
def estudio_finalizado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.ENVIADA_EXTERIOR):
        estudio.estado = EstadoEstudio.FINALIZADO
        return True, estudio
    else:
        return False, estudio
    
def estudio_cancelado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    estudio.estado = EstadoEstudio.CANCELADO
    return True, estudio

def estudio(request, estudio_id):
    estudio = get_object_or_404(Estudio, id_estudio=estudio_id)
    return render(request, "estudio.html", {"estudio": estudio})