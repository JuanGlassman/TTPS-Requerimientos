from django.shortcuts import render, get_object_or_404, redirect
from estudios.models import Estudio, EstadoEstudio
from estudios import views as estudio_estado
from .models import Presupuesto
from estudios import views as estudio_view
from transportista.views import agregar_estudio_a_pedido
from django.contrib.auth.decorators import login_required
from inicio_sesion.views import permission_required

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
    costo_hallazgos_secundario = request.POST.get('costo_hallazgos_secundarios')
    id_presupuesto = request.POST.get('id_presupuesto')

    presupuesto = get_object_or_404(Presupuesto, id_presupuesto=id_presupuesto)
    presupuesto.costo_exoma = costo_exoma
    presupuesto.costo_genes_extra = costo_genes_extra 
    presupuesto.costo_hallazgos_secundarios = costo_hallazgos_secundario   
    presupuesto.total = float(costo_genes_extra) + float(costo_exoma) + float(costo_hallazgos_secundario)

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

@login_required
@permission_required('pedido_create')
@permission_required('pedido_update')
@permission_required('ruta_create')
@permission_required('ruta_update')
def realizar_estudio(request, estudio_id):
    estudio = get_object_or_404(Estudio, id_estudio=estudio_id)
    response = agregar_estudio_a_pedido(estudio_id)
    res, estudio = estudio_estado.estudio_realizado(estudio)
    estudio.save()
    return redirect('lab_admin:estudios')

def form_resultado(request, estudio_id):
    estudio = get_object_or_404(Estudio, id_estudio=estudio_id)
    render(request, "resultado_estudio.html", { "estudio": estudio })

def cargar_resultado(request):
    pass