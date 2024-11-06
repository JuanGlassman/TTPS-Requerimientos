from django.shortcuts import render, get_object_or_404, redirect
from estudios.models import Estudio, EstadoEstudio
from estudios import views as estudio_estado
from .models import Presupuesto
from estudios import views as estudio_view

def estudios(request):
    estudios = Estudio.objects.order_by("fecha")
    return render(request, "estudios.html", { "estudios": estudios, "estados": EstadoEstudio })

def form_presupuesto(request, estudio_id):
    estudio = get_object_or_404(Estudio, id_estudio=estudio_id)

    if (estudio.estado == EstadoEstudio.INICIADO):
        presupuesto = get_object_or_404(Presupuesto, estudio_id=estudio_id)
        return render(request, "editar_presupuesto.html", {
            "presupuesto": presupuesto,
            "estudio": estudio
        })
    else:
        #informar que no se puede presupuestar un estudio que no esta en estado iniciado
        return redirect('estudios')

def presupuestar(request):
    costo_exoma = request.POST.get('costo_exoma')
    costo_genes_extra = request.POST.get('costo_genes_extra')
    id_presupuesto = request.POST.get('id_presupuesto')

    presupuesto = get_object_or_404(Presupuesto, id_presupuesto=id_presupuesto)
    presupuesto.costo_exoma = costo_exoma
    presupuesto.costo_genes_extra = costo_genes_extra    

    estudio = get_object_or_404(Estudio, id_estudio=presupuesto.estudio_id)
    res, estudio = estudio_view.estudio_presupuestado(estudio)
    if (res):
        presupuesto.save()
        estudio.save()
    return redirect(f'/estudios/{estudio.id_estudio}')

def pagar_admin(request, estudio_id):
    estudio = get_object_or_404(Estudio, id_estudio=estudio_id)
    res, estudio = estudio_estado.estudio_pagado(estudio)
    estudio.save()    
    return render(request, "estudio.html", {'estudio': estudio})

def cancelar_estudio(request, estudio_id):
    estudio = get_object_or_404(Estudio, id_estudio=estudio_id)
    res, estudio = estudio_estado.estudio_cancelado(estudio)
    estudio.save()    
    return render(request, "estudio.html", {'estudio': estudio})