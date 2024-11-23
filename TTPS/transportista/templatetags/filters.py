# transportista/templatetags/filters.py
from django import template

register = template.Library()

@register.filter
def filtrar_pendientes(queryset, estado):
    return queryset.filter(estado=estado)