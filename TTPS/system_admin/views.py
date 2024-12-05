from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from inicio_sesion.models import Usuario, Rol
from medicos.models import Medico
from lab_admin.models import LabAdmin
from lab_admin.models import Centro
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inicio_sesion.views import permission_required
from .forms import UsuarioForm, MedicoForm, CentroForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from TTPS.settings import EMAIL_HOST_PASSWORD

@login_required
@permission_required('lista_usuarios')
def lista_usuarios(request):
    usuarios = Usuario.objects.filter(is_deleted=False).exclude(dni=1).order_by('dni')  # Ordena por DNI
    paginator = Paginator(usuarios, 10)  # 10 usuarios por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista_usuarios.html', {'object_list': page_obj, 'activated': True})

@login_required
@permission_required('lista_usuarios')
def lista_usuarios_desactivados(request):
    usuarios = Usuario.objects.filter(is_deleted=True)
    paginator = Paginator(usuarios, 10)  # 10 usuarios por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista_usuarios.html', {'object_list': page_obj, 'activated': False})

@login_required
@permission_required('usuario_destroy')
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.is_deleted = True
    usuario.save()
    messages.success(request, "Usuario eliminado correctamente.")
    return redirect('system_admin:lista_usuarios')

@login_required
@permission_required('usuario_update')
def activar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.is_deleted = False
    usuario.save()
    messages.success(request, "Usuario activado correctamente.")
    return redirect('system_admin:usuarios_desactivados')

@login_required
@permission_required('lista_medicos')
def lista_medicos(request):
    medicos = Medico.objects.filter(usuario__is_deleted=False)
    paginator = Paginator(medicos, 10)  # 10 usuarios por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista_medicos.html', {'object_list': page_obj, 'activated': True})
    
@login_required
@permission_required('lista_medicos')
def lista_medicos_desactivados(request):
    medicos = Medico.objects.filter(usuario__is_deleted=True)
    paginator = Paginator(medicos, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista_medicos.html', {'object_list': page_obj, 'activated': False})

@login_required
@permission_required('medico_create')
@transaction.atomic
def crear_medico_view(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        medico_form = MedicoForm(request.POST)

        if usuario_form.is_valid() and medico_form.is_valid():
            rol = get_object_or_404(Rol, nombre='medico')
            usuario, password = usuario_form.save(rol=rol)
            medico = medico_form.save(commit=False)
            medico.usuario = usuario
            medico.save()
            enviar_correo_nuevo_usuario(usuario, password)
            return redirect('system_admin:lista_medicos')

    else:
        usuario_form = UsuarioForm()
        medico_form = MedicoForm()

    context = {
        'usuario_form': usuario_form,
        'medico_form': medico_form,
    }
    return render(request, 'crear_medico.html', context)

@login_required
@permission_required('medico_update')
def editar_medico_view(request, medico_id):
    medico = get_object_or_404(Medico, pk=medico_id)
    usuario_form = UsuarioForm(request.POST or None, instance=medico.usuario)
    medico_form = MedicoForm(request.POST or None, instance=medico)

    if request.method == 'POST':
        if usuario_form.is_valid() and medico_form.is_valid():
            usuario_form.save()
            medico_form.save()
            return redirect('system_admin:lista_medicos')

    context = {
        'usuario_form': usuario_form,
        'medico_form': medico_form,
        'medico': medico,
    }

    return render(request, 'editar_medico.html', context)

@login_required
@permission_required('lista_lab_admin')
def lista_lab_admins(request):
    lab_admins = LabAdmin.objects.filter(usuario__is_deleted=False)
    paginator = Paginator(lab_admins, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista_lab_admins.html', {'object_list': page_obj, 'activated': True})

@login_required
@permission_required('lista_lab_admin')
def lista_lab_admins_desactivados(request):
    lab_admins = LabAdmin.objects.filter(usuario__is_deleted=True)
    paginator = Paginator(lab_admins, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista_lab_admins.html', {'object_list': page_obj, 'activated': False})

@login_required
@permission_required('lab_admin_create')
def crear_lab_admin_view(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)

        if usuario_form.is_valid():
            usuario, password = usuario_form.save(commit=False)
            rol = get_object_or_404(Rol, nombre='lab_admin')
            usuario.username = usuario.dni
            usuario.rol = rol
            usuario.save()
            lab_admin = LabAdmin(usuario=usuario)
            lab_admin.save()
            enviar_correo_nuevo_usuario(usuario, password)
            return redirect('system_admin:lista_lab_admins')

    else:
        usuario_form = UsuarioForm()

    context = {
        'usuario_form': usuario_form,
    }
    return render(request, 'crear_lab_admin.html', context)

@login_required
@permission_required('lab_admin_create')
def editar_lab_admin_view(request, id_lab_admin):
    lab_admin = get_object_or_404(LabAdmin, pk=id_lab_admin)
    usuario_form = UsuarioForm(request.POST or None, instance=lab_admin.usuario)

    if request.method == 'POST':
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('system_admin:lista_lab_admins')

    context = {
        'usuario_form': usuario_form,
        'lab_admin': lab_admin,
    }

    return render(request, 'editar_lab_admin.html', context)

@login_required
@permission_required('lista_centros')
def lista_centros(request):
    centros = Centro.objects.filter(is_deleted=False)
    paginator = Paginator(centros, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista_centros.html', {'object_list': page_obj})

@login_required
@permission_required('centro_create')
def crear_centro(request):
    if request.method == 'POST':
        form = CentroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('system_admin:lista_centros')
    else:
        form = CentroForm()
    return render(request, 'formulario_centro.html', {'form': form})

@login_required
@permission_required('centro_update')
def editar_centro(request, pk):
    centro = get_object_or_404(Centro, pk=pk)
    if request.method == 'POST':
        form = CentroForm(request.POST, instance=centro)
        if form.is_valid():
            form.save()
            return redirect('system_admin:lista_centros')
    else:
        form = CentroForm(instance=centro)
    return render(request, 'formulario_centro.html', {'form': form})

@login_required
@permission_required('centro_destroy')
def eliminar_centro(request, pk):
    centro = get_object_or_404(Centro, pk=pk)
    centro.is_deleted = True
    centro.save()
    messages.success(request, "Centro eliminado correctamente.")
    return redirect('system_admin:lista_centros')

@login_required
@permission_required('centro_update')
def activar_centro(request, pk):
    centro = get_object_or_404(Centro, pk=pk)
    centro.is_deleted = False
    centro.save()
    messages.success(request, "Centro activado correctamente.")
    return redirect('system_admin:centros_desactivados')

@login_required
@permission_required('centro_create')
def lista_centros_desactivados(request):
    centros = Centro.objects.filter(is_deleted=True)
    paginator = Paginator(centros, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista_centros.html', {'object_list': page_obj, 'activated': False})


def enviar_correo_nuevo_usuario(usuario, password):
        """Envía un correo electrónico al usuario con el nombre de usuario y la contraseña recién creados"""
        try:
            subject = "Bienvenido a la plataforma"
            context = {
                'usuario': usuario,
                'password': password #se envia por parametro porque se utilizamos usuario.password esta hasheada
            }
            body = render_to_string("mail_nuevo_usuario.html", context)

            message = Mail(
                from_email='laboratorios_laplata@hotmail.com',  
                to_emails=usuario.email,
                subject=subject,
                html_content=body
            )

            sg = SendGridAPIClient(EMAIL_HOST_PASSWORD)
            response = sg.send(message)

            print(f"Correo enviado con código de estado: {response.status_code}")
            if response.body:
                print(f"Respuesta del servidor: {response.body}")

        except Exception as e:
            print(f"Error al enviar correo: {e}")


@login_required
@permission_required('usuario_update')
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('system_admin:lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'formulario_usuario.html', {'form': form})