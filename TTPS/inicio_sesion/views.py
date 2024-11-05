from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .models import Usuario
from django.contrib.auth.hashers import check_password

def find_user_by_dni(dni):
    """Busca un usuario por su dni"""
    return Usuario.objects.filter(dni=dni).first()

def user_deleted(user):
    return user.is_deleted == True

def check_user(dni, password):
    """Verifica las credenciales del usuario"""
    user = find_user_by_dni(dni)

    if user and check_password(password, user.password):
        print(f"Usuario autenticado: {user.email}, id: {user.id}")
        return user
    
    return None


def authenticate(request, dni, password):
    user = check_user(dni, password)

    if not user:
        messages.error(request, "Usuario o contraseña incorrectos")
        return False
    
    if user_deleted(user):
        messages.error(request, "Usuario eliminado")
        return False
    
    
    
    messages.success(request, "La sesión se inició correctamente")
    return user 

def login_view(request):
    if request.method == 'POST':
        dni = request.POST['dni']
        password = request.POST['password']
        user = authenticate(request, dni, password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, "La sesión se inició correctamente")
                return redirect('inicio_sesion:perfil')
            else:
                messages.error(request, "Usuario bloqueado o eliminado.")
        return redirect('inicio_sesion:login')

    return render(request, 'login.html')

@login_required
def perfil_view(request):
    return render(request, 'change_password.html')



@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "La sesión se cerró correctamente")
    return redirect('home')



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
