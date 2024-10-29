from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.rol.nombre in allowed_roles:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "La sesión se inició correctamente")
                return redirect('home')
            else:
                messages.error(request, "Usuario bloqueado o eliminado.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
        return redirect('login')

    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "La sesión se cerró correctamente")
    return redirect('home')

