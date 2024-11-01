from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import AnonymousUser

# Usado para mostrar el rol del usuario en cualquier momento
# como contex_processors en settings.py TEMPLATES
def user_role(request):
    # Verifica si el usuario está autenticado y tiene un rol
    if isinstance(request.user, AnonymousUser):
        return {'user_role': None}
    elif hasattr(request.user, 'rol') and request.user.rol:
        return {'user_role': request.user.rol.nombre}
    return {'user_role': None}

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.rol.nombre in allowed_roles:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator

#def login_view(request):
#    if request.method == 'POST':
#        email = request.POST['email']
#        password = request.POST['password']
#        user = authenticate(request, username=email, password=password)
#
#        if user is not None:
#            if user.is_active:
#                login(request, user)
#                messages.success(request, "La sesión se inició correctamente")
#                return redirect('home')
#            else:
#                messages.error(request, "Usuario bloqueado o eliminado.")
#        else:
#            messages.error(request, "Usuario o contraseña incorrectos")
#        return redirect('login')
#
#    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        dni = request.POST['dni']
        password = request.POST['password']
        user = authenticate(request, username=dni, password=password)
        print(user)
        if user is not None:
            print("1")
            if user.is_active:
                print("2")
                login(request, user)
                print("3")
                messages.success(request, "La sesión se inició correctamente")
            else:
                messages.error(request, "Usuario bloqueado o eliminado.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
        return redirect('inicio_sesion:login')

    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "La sesión se cerró correctamente")
    return redirect('home')

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

@login_required
def cambiar_contrasena_view(request):
    if request.method == 'POST':
        password1 = request.POST.get("current_password")
        password2 = request.POST.get("new_password")
        password3 = request.POST.get("new_password_again")
        
        # Verificar que todos los campos estén llenos
        if not password1 or not password2 or not password3:
            messages.warning(request, "Todos los campos son obligatorios.")
            return render(request, 'auth/change_password.html')
        
        # Verificar la contraseña actual
        if not request.user.check_password(password1):
            messages.error(request, "La contraseña actual es incorrecta.")
            return render(request, 'auth/change_password.html')

        # Verificar que las contraseñas nuevas coincidan
        if password2 != password3:
            messages.error(request, "Las nuevas contraseñas no coinciden.")
            return render(request, 'auth/change_password.html')
        
        # Cambiar la contraseña
        try:
            request.user.set_password(password2)
            request.user.save()
            update_session_auth_hash(request, request.user)  # Mantener la sesión iniciada
            messages.success(request, "Contraseña cambiada exitosamente.")
            return redirect('home')  # Redirigir a la página de inicio o a otra vista
        except Exception as e:
            messages.error(request, f"Error al cambiar la contraseña: {str(e)}")
        
    return render(request, 'auth/change_password.html')
