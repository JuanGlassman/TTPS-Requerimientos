from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from inicio_sesion.views import permission_required
from .models import Pedido, HojaDeRuta
from datetime import date
from django import template

register = template.Library()

@register.filter
def filtrar_pendientes(queryset, estado):
    return queryset.filter(estado=estado)

@login_required
@permission_required('transportista')
def lista_pedidos(request):
    hoja_de_ruta = HojaDeRuta.objects.filter(fecha=date.today(), transportista=request.user.transportista)
    return render(request, 'lista_pedidos.html', {'hoja_de_ruta': hoja_de_ruta})