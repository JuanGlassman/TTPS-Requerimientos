from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from estudios.models import Estudio, EstadoEstudio, HistorialEstudio
from datetime import datetime

def estudio_terminado(estudio):
    return estudio.estado in [EstadoEstudio.CANCELADO, EstadoEstudio.FINALIZADO]

def registrar_historial(estudio, estado_anterior, estado_nuevo):
    h = get_object_or_404(HistorialEstudio,
        estudio_id = estudio.id_estudio,
        estado = estado_anterior
    )
    h.fecha_fin = datetime.now()
    h.save()
    HistorialEstudio.objects.create(
        estudio_id = estudio.id_estudio,
        estado = estado_nuevo
    )

def estudio_iniciado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if estudio.estado == EstadoEstudio.INICIADO:
        h = HistorialEstudio.objects.create(
            estudio_id = estudio.id_estudio,
            estado = estudio.estado
        )
    return True, estudio

def estudio_presupuestado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.INICIADO):
        estudio.estado = EstadoEstudio.PRESUPUESTADO
        registrar_historial(estudio, EstadoEstudio.INICIADO, EstadoEstudio.PRESUPUESTADO)
        return True, estudio
    else:
        return False, estudio

def estudio_pagado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.PRESUPUESTADO):
        estudio.estado = EstadoEstudio.PAGADO
        registrar_historial(estudio, EstadoEstudio.PRESUPUESTADO, EstadoEstudio.PAGADO)
        return True, estudio
    else:
        return False, estudio

def estudio_autorizado(estudio):
    if estudio_terminado(estudio):
        return False, estudio

    if (estudio.estado == EstadoEstudio.PAGADO):
        estudio.estado = EstadoEstudio.AUTORIZADO
        registrar_historial(estudio, EstadoEstudio.PAGADO, EstadoEstudio.AUTORIZADO)
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
    return render(request, "estudio.html", {"estudio": estudio, "estados": EstadoEstudio})