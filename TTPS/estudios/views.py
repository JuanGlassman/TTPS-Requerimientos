from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from estudios.models import Estudio, EstadoEstudio, HistorialEstudio, SampleSet
from datetime import datetime
from django.db.models import Count

def estudio_terminado(estudio):
    return estudio.estado in [EstadoEstudio.CANCELADO, EstadoEstudio.FINALIZADO]

def registrar_historial(estudio, estado_anterior, estado_nuevo):
    try:
        historial = HistorialEstudio.objects.filter(
            estudio_id=estudio.id_estudio,
            estado=estado_anterior
        ).first()

        if historial:
            historial.fecha_fin = datetime.now()
            historial.save()
        else:
            print(f"No se encontró un historial para el estudio {estudio.id_estudio} con estado {estado_anterior}.")


        HistorialEstudio.objects.create(
            estudio_id = estudio.id_estudio,
            estado = estado_nuevo
        )
    except Exception as e:
        print(f"Error al registrar el historial: {e}")
        raise

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
    res = True
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.INICIADO):
        estudio.estado = EstadoEstudio.PRESUPUESTADO
        registrar_historial(estudio, EstadoEstudio.INICIADO, EstadoEstudio.PRESUPUESTADO)
        return res, estudio
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
        registrar_historial(estudio, EstadoEstudio.AUTORIZADO, EstadoEstudio.TURNO_CONFIRMADO)
        return True, estudio
    else:
        return False, estudio

def estudio_realizado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.TURNO_CONFIRMADO):
        estudio.estado = EstadoEstudio.REALIZADA
        registrar_historial(estudio, EstadoEstudio.TURNO_CONFIRMADO, EstadoEstudio.REALIZADA)
        return True, estudio
    else:
        return False, estudio

def estudio_centralizado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.REALIZADA):
        estudio.estado = EstadoEstudio.CENTRALIZADA
        asignar_a_sample_set(estudio)
        registrar_historial(estudio, EstadoEstudio.REALIZADA, EstadoEstudio.CENTRALIZADA)
        return True, estudio
    else:
        return False, estudio

def estudio_enviado_exterior(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.CENTRALIZADA):
        estudio.estado = EstadoEstudio.ENVIADA_EXTERIOR
        registrar_historial(estudio, EstadoEstudio.CENTRALIZADA, EstadoEstudio.ENVIADA_EXTERIOR)
        return True, estudio
    else:
        return False, estudio
    
def estudio_finalizado(estudio):
    if estudio_terminado(estudio):
        return False, estudio
    if (estudio.estado == EstadoEstudio.ENVIADA_EXTERIOR):
        estudio.estado = EstadoEstudio.FINALIZADO
        registrar_historial(estudio, EstadoEstudio.ENVIADA_EXTERIOR, EstadoEstudio.FINALIZADO)
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



def asignar_a_sample_set(estudio):
    sample_set = SampleSet.objects.annotate(estudio_count=Count('estudios')).filter(
        fecha_envio__isnull=True,
        estudio_count__lt=100
    ).first()

    if not sample_set:
        sample_set = SampleSet.objects.create()

    estudio.sample_set = sample_set
    estudio.save()

    sample_set.estudios.add(estudio)
    sample_set.save()

    return sample_set


