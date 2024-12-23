from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from inicio_sesion.views import permission_required
from .models import Pedido, HojaDeRuta, Transportista
from datetime import date, time, timedelta
from estudios.models import Estudio
from lab_admin.models import Centro, Turno
import base64, json
from estudios.views import estudio_centralizado

@login_required
@permission_required('transportista')
def lista_pedidos(request):
    transportista = Transportista.objects.get(usuario=request.user)
    hoja_de_ruta = HojaDeRuta.objects.filter(fecha=date.today()).filter(transportista=transportista).first()
    if (hoja_de_ruta is None):
        return render(request, 'lista_pedidos.html', {'hoja_de_ruta': None, 'pedidos': [], 'pendientes': 0})
    pedidos = []
    # Recorro y enlisto pedidos pendientes
    # Si ordenamos aca para mapa, tenerlo en cuenta
    for pedido in hoja_de_ruta.pedidos.all():
        if pedido.estado == 'pendiente':
            pedidos.append(pedido)
    # Los cuento para mensaje en front
    pedidos_pendientes = len(pedidos)
    # Recorro y enlisto pedidos finalizados
    for pedido in hoja_de_ruta.pedidos.all():
        if pedido.estado == 'finalizado':
            pedidos.append(pedido)
    print (hoja_de_ruta)
    return render(request, 'lista_pedidos.html', {'hoja_de_ruta': hoja_de_ruta, 'pedidos': pedidos, 'pendientes': pedidos_pendientes})

def crear_pedido(estudio, centro_id):
    pedido = Pedido.objects.create(centro_id=centro_id, estado='pendiente')
    pedido.estudios.add(estudio)
    pedido.save()
    return pedido

def crear_hoja_de_ruta(pedido):
    transportista_id = Transportista.objects.first().id_transportista
    ## Esta es la linea correcta
    hoja_de_ruta = HojaDeRuta.objects.create(transportista_id=transportista_id, fecha=date.today() + timedelta(days=1), estado='pendiente')
    ## Esta es la linea por razones de demo
    #hoja_de_ruta = HojaDeRuta.objects.create(transportista_id=transportista_id, fecha=date.today(), estado='pendiente')
    hoja_de_ruta.pedidos.add(pedido)
    hoja_de_ruta.save()
    return hoja_de_ruta

def agregar_pedido_a_hoja_de_ruta(pedido, hoja_de_ruta_id):
    hoja_de_ruta = HojaDeRuta.objects.get(id_hoja_de_ruta=hoja_de_ruta_id)
    hoja_de_ruta.pedidos.add(pedido)
    hoja_de_ruta.save()
    return hoja_de_ruta

def buscar_hoja_de_ruta_pendiente_por_fecha(fecha):
    return HojaDeRuta.objects.filter(fecha=fecha).filter(estado='pendiente')

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
    ## Esta es la linea correcta
    hoja_de_ruta = buscar_hoja_de_ruta_pendiente_por_fecha(date.today() + timedelta(days=1)).first()
    ## Esta es la linea por razones de demo
    #hoja_de_ruta = buscar_hoja_de_ruta_pendiente_por_fecha(date.today()).first()
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

@login_required
@permission_required('transportista')
def ver_mapa(request, hoja_id):
    hoja = get_object_or_404(HojaDeRuta, id_hoja_de_ruta=hoja_id)
    centros = Centro.objects.filter(pedido__in=hoja.pedidos.filter(estado='pendiente')).distinct()
    print(centros)
    return render(request, 'mapa_pedidos.html',  {"centros": centros})

@login_required
@permission_required('transportista')
def ver_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id_pedido=pedido_id)
    return render(request, 'ver_pedido.html', {'pedido': pedido})

@login_required
@permission_required('transportista')
def iniciar_recorrido(request, hoja_id):
    hoja = get_object_or_404(HojaDeRuta, id_hoja_de_ruta=hoja_id)
    cambiar_estado_hoja(hoja, 'en_curso')
    return redirect('transportista:lista_pedidos')

def cargar_resultados(hoja):
    for pedido in hoja.pedidos.all():
        for estudio in pedido.estudios.all():
            estudio_centralizado(estudio)


@login_required
@permission_required('transportista')
def finalizar_recorrido(request, hoja_id):
    hoja = get_object_or_404(HojaDeRuta, id_hoja_de_ruta=hoja_id)
    cambiar_estado_hoja(hoja, 'finalizada')
    cargar_resultados(hoja)
    return redirect('transportista:lista_pedidos')

def cambiar_estado_hoja(hoja_de_ruta, estado):
    estados = ['pendiente', 'en_curso', 'finalizada']
    if estado not in estados:
        return hoja_de_ruta
    if (estado == 'en_curso'):
        hoja_de_ruta.hora_comienzo = timezone.localtime(timezone.now()).time()
    elif (estado == 'finalizada'):
        hoja_de_ruta.hora_fin = timezone.localtime(timezone.now()).time()
    hoja_de_ruta.estado = estado
    hoja_de_ruta.save()
    return hoja_de_ruta

@login_required
@permission_required('transportista')
def entregar_pedido(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            print(f"DATA pedido entregado: {data} ")
            pedido_id = data.get('pedido_id')
            firma = data.get('firma')
            observacion = data.get('observaciones')
            pedido = Pedido.objects.get(id_pedido=pedido_id)
            if (pedido is None):
                return JsonResponse({'success': False}, status=404)
            pedido.estado = 'finalizado'
            pedido.firma = firma
            pedido.observacion = observacion
            pedido.save()
            return JsonResponse({'success': True}, status=200)
    except Exception as e:
        print(f"ERROR: {e}")
        return JsonResponse({'success': False}, status=500)
    
@login_required
@permission_required('transportista')
def cancelar_pedido(request, pedido_id):
    # Si el transportista no puede recoger el pedido, lo cancela
    # entonces el pedido se agrega a la hoja de ruta del dia de mañana.
    pedido = get_object_or_404(Pedido, id_pedido=pedido_id)
    ## Esta es la linea correcta
    hoja_de_ruta = buscar_hoja_de_ruta_pendiente_por_fecha(date.today() + timedelta(days=1)).first()
    ## Esta es la linea por razones de demo
    #hoja_de_ruta = buscar_hoja_de_ruta_pendiente_por_fecha(date.today()).first()
    if not hoja_de_ruta:
        hoja_de_ruta = crear_hoja_de_ruta(pedido)
    else:
        hoja_de_ruta.pedidos.add(pedido)
        hoja_de_ruta.save()
    hoja_de_ruta_hoy = buscar_hoja_de_ruta_por_fecha(date.today()).first()
    hoja_de_ruta_hoy.pedidos.remove(pedido)
    hoja_de_ruta_hoy.save()
    return redirect('transportista:lista_pedidos')