from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from inicio_sesion.views import permission_required
from .models import Pedido, HojaDeRuta, Transportista
from datetime import date, time, timedelta
from estudios.models import Estudio
from lab_admin.models import Centro, Turno

@login_required
@permission_required('transportista')
def lista_pedidos(request):
    transportista = Transportista.objects.get(usuario=request.user)
    hoja_de_ruta = HojaDeRuta.objects.filter(fecha=date.today()).filter(transportista=transportista).first()
    print (hoja_de_ruta)
    return render(request, 'lista_pedidos.html', {'hoja_de_ruta': hoja_de_ruta})

def crear_pedido(estudio, centro_id):
    pedido = Pedido.objects.create(centro_id=centro_id, estado='pendiente')
    pedido.estudios.add(estudio)
    pedido.save()
    return pedido

def crear_hoja_de_ruta(pedido):
    transportista_id = Transportista.objects.first().id_transportista
    hoja_de_ruta = HojaDeRuta.objects.create(transportista_id=transportista_id, fecha=date.today() + timedelta(days=1), estado='pendiente')
    hoja_de_ruta.pedidos.add(pedido)
    hoja_de_ruta.save()
    return hoja_de_ruta

def agregar_pedido_a_hoja_de_ruta(pedido, hoja_de_ruta_id):
    hoja_de_ruta = HojaDeRuta.objects.get(id=hoja_de_ruta_id)
    hoja_de_ruta.pedidos.add(pedido)
    hoja_de_ruta.save()
    return hoja_de_ruta

def buscar_hoja_de_ruta_por_fecha(fecha):
    return HojaDeRuta.objects.filter(fecha=fecha)

def agregar_estudio_a_pedido(estudio_id):
    # busco hoja de ruta del dia de mañana
    # si no existe creo una hoja de ruta para mañana creando un pedido para el centro del estudio con el estudio
    # busco pedidos de esa hoja de ruta si existe alguno para el centro del estudio agrego el estudio a ese pedido
    # si no existe creo un pedido y lo agrego a la hoja de ruta
    estudio = Estudio.objects.get(id_estudio=estudio_id)
    turno = Turno.objects.get(estudio=estudio)
    centro_id = turno.centro.id_centro
    hoja_de_ruta = buscar_hoja_de_ruta_por_fecha(date.today() + timedelta(days=1)).first()
    if not hoja_de_ruta:
        pedido = crear_pedido(estudio, centro_id)
        hoja_de_ruta = crear_hoja_de_ruta(pedido)
    else:
        for pedido in hoja_de_ruta.pedidos.all():
            if pedido.centro.id_centro == centro_id:
                pedido.estudios.add(estudio)
                pedido.save()
                return True
        pedido = crear_pedido(estudio, centro_id)
        hoja_de_ruta = agregar_pedido_a_hoja_de_ruta(pedido, hoja_de_ruta.id_hoja_de_ruta)
    pedido.estudios.add(estudio)
    pedido.save()
    return True