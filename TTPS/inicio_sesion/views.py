from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, authenticate, login
from .forms import LoginForm
from django.contrib.auth import get_user_model
from .models import Rol
from django.core.exceptions import PermissionDenied
from functools import wraps
from .utils import PERMISOS_POR_ROL
from medicos.models import Medico
from pacientes.models import Paciente

def permission_required(permiso_requerido):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied 

            rol_usuario = request.user.rol.nombre 

            # Verifica si el rol del usuario tiene el permiso requerido
            if rol_usuario in PERMISOS_POR_ROL and permiso_requerido in PERMISOS_POR_ROL[rol_usuario]:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied  
        return _wrapped_view
    return decorator


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
            
            user = authenticate(request, dni=dni, password=password)
            if user is not None:
                login(request, user)
                if user.first_login:
                    messages.info(request, "Es tu primer inicio de sesión. Cambia tu contraseña.")
                    return redirect('inicio_sesion:cambiar_contrasena') 
                else:
                    messages.success(request, "Inicio de sesión exitoso.")
                    return redirect('home')
            else:
                messages.error(request, "DNI o contraseña incorrectos.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


@login_required
def perfil_view(request):
    user = request.user
    medico = None
    paciente = None

    if hasattr(user, 'medico'):
        medico = user.medico
    elif hasattr(user, 'paciente'):
        paciente = user.paciente

    context = {
        'user': user,
        'medico': medico,
        'paciente': paciente,
    }
    return render(request, 'profile.html', context)


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "La sesión se cerró correctamente")
    return redirect('home')


@login_required
def cambiar_contrasena_view(request):
    user = request.user

    if request.method == 'POST':
        if user.first_login:
            password1 = user.password
        else:
            password1 = request.POST.get("current_password")
        
        password2 = request.POST.get("new_password")
        password3 = request.POST.get("new_password_again")
        
        if not user.first_login and not password1:
            messages.warning(request, "La contraseña actual es obligatoria.")
            return render(request, 'change_password.html')
        if not password2 or not password3:
            messages.warning(request, "Los campos de la nueva contraseña son obligatorios.")
            return render(request, 'change_password.html')
        
        # Verificar la contraseña actual, excepto en el primer inicio de sesión
        if not user.first_login and not user.check_password(password1):
            messages.error(request, "La contraseña actual es incorrecta.")
            return render(request, 'change_password.html')

        # Verificar que las contraseñas nuevas coincidan
        if password2 != password3:
            messages.error(request, "Las nuevas contraseñas no coinciden.")
            return render(request, 'change_password.html')
        
        try:
            user.first_login = False
            user.set_password(password2)
            user.save()
            update_session_auth_hash(request, user) 
            messages.success(request, "Contraseña cambiada exitosamente.")
            return redirect('home')  
        except Exception as e:
            messages.error(request, f"Error al cambiar la contraseña: {str(e)}")
        
    return render(request, 'change_password.html')


@login_required
def editar_perfil_medico(request, medico):
    especialidad = request.POST.get('especialidad')
    matricula = request.POST.get('matricula')

    medico.especialidad = especialidad
    medico.matricula = matricula
    medico.save()

@login_required
def editar_perfil_paciente(request, paciente):
    antecedentes = request.POST.get('antecedentes')
    historial_medico = request.POST.get('historial_medico')

    paciente.antecedentes = antecedentes
    paciente.historial_medico = historial_medico
    paciente.save()

@login_required
def actualizar_usuario_basico(request, user):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    genero = request.POST.get('genero')

    user.first_name = first_name
    user.last_name = last_name
    user.fecha_nacimiento = fecha_nacimiento
    user.genero = genero
    user.save()


@login_required
def editar_perfil(request):
    user = request.user

    medico = None
    paciente = None

    if hasattr(user, 'medico'):
        medico = user.medico
    elif hasattr(user, 'paciente'):
        paciente = user.paciente

    if request.method == 'POST':
        actualizar_usuario_basico(request, user)

        if medico:
            editar_perfil_medico(request, medico)

        if paciente:
            editar_perfil_paciente(request, paciente)

        messages.success(request, "Perfil actualizado correctamente.")
        return redirect('inicio_sesion:perfil')

    roles = Rol.objects.all()

    context = {
        'user': user,
        'roles': roles,
        'medico': medico,
        'paciente': paciente,
    }
    return render(request, 'edit_profile.html', context)
