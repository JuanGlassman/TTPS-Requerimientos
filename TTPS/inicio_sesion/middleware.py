from django.shortcuts import redirect
from django.urls import reverse

class FirstLoginMiddleware:
    """
    Middleware para redirigir a los usuarios que aún no han cambiado su contraseña.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica si el usuario está autenticado y si es su primer inicio de sesión
        if request.user.is_authenticated and request.user.first_login:
            # Permitir solo la página de cambio de contraseña y el cierre de sesión
            allowed_urls = [
                reverse('inicio_sesion:cambiar_contrasena'),  # Cambiar contraseña
                reverse('inicio_sesion:logout'),              # Cerrar sesión
            ]
            if request.path not in allowed_urls:
                return redirect('inicio_sesion:cambiar_contrasena')
        
        response = self.get_response(request)
        return response
