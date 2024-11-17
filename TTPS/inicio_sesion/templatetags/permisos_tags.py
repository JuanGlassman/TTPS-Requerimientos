# inicio_sesion/templatetags/permisos_tags.py
from django import template
from inicio_sesion.views import PERMISOS_POR_ROL  # Ajusta la importación según tu proyecto

register = template.Library()

@register.simple_tag
def tiene_permiso(usuario, permiso):
    if usuario.is_authenticated:
        rol_usuario = usuario.rol.nombre  # Obtiene el rol del usuario
        return permiso in PERMISOS_POR_ROL.get(rol_usuario, [])
    return False
