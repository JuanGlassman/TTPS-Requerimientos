# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import get_user_model


def authenticate(request, dni=None, password=None):
    User = get_user_model()
    try:
        user = User.objects.get(dni=dni)
        if user.check_password(password):
            return user
    except User.DoesNotExist:
        return None


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data.get('dni')
            password = form.cleaned_data.get('password')
            
            # Autentica al usuario usando el modelo personalizado
            user = authenticate(request, dni=dni, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Inicio de sesión exitoso.")
                return redirect('inicio')  # Cambia 'inicio' por la vista de inicio de tu aplicación
            else:
                messages.error(request, "DNI o contraseña incorrectos.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})
