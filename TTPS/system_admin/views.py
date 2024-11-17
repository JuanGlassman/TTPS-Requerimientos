from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.db import transaction
from inicio_sesion.models import Usuario
from inicio_sesion.models import Rol
from medicos.models import Medico
from lab_admin.models import LabAdmin
from lab_admin.models import Centro
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inicio_sesion.views import permission_required
from .forms import UsuarioForm, MedicoForm, CentroForm, UsuarioRolForm

@login_required
@permission_required('lista_usuarios')
def lista_usuarios(request):
    usuarios = Usuario.objects.filter(is_deleted=False)
    return render(request, 'lista_usuarios.html', {'object_list': usuarios, 'activated': True})

@login_required
@permission_required('lista_usuarios')
def lista_usuarios_desactivados(request):
    usuarios = Usuario.objects.filter(is_deleted=True)
    return render(request, 'lista_usuarios.html', {'object_list': usuarios, 'activated': False})

@login_required
@permission_required('usuario_create')
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioRolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('system_admin:lista_usuarios')
    else:
        form = UsuarioRolForm()
    return render(request, 'formulario_usuario.html', {'form': form})

@login_required
@permission_required('usuario_update')
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioRolForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('system_admin:lista_usuarios')
    else:
        form = UsuarioRolForm(instance=usuario)
    return render(request, 'formulario_usuario.html', {'form': form})

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
    return render(request, 'lista_medicos.html', {'object_list': medicos, 'activated': True})
    
@login_required
@permission_required('lista_medicos')
def lista_medicos_desactivados(request):
    medicos = Medico.objects.filter(usuario__is_deleted=True)
    return render(request, 'lista_medicos.html', {'object_list': medicos, 'activated': False})

@login_required
@permission_required('medico_create')
@transaction.atomic
def crear_medico_view(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        medico_form = MedicoForm(request.POST)

        if usuario_form.is_valid() and medico_form.is_valid():
            rol = get_object_or_404(Rol, nombre='medico')
            usuario = usuario_form.save(rol=rol)
            medico = medico_form.save(commit=False)
            medico.usuario = usuario
            medico.save()
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
    return render(request, 'lista_lab_admins.html', {'object_list': lab_admins, 'activated': True})

@login_required
@permission_required('lista_lab_admin')
def lista_lab_admins_desactivados(request):
    lab_admins = LabAdmin.objects.filter(usuario__is_deleted=True)
    return render(request, 'lista_lab_admins.html', {'object_list': lab_admins, 'activated': False})

@login_required
@permission_required('lab_admin_create')
def crear_lab_admin_view(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)

        if usuario_form.is_valid():
            usuario = usuario_form.save(commit=False)
            rol = get_object_or_404(Rol, nombre='lab_admin')
            usuario.username = usuario.dni
            usuario.rol = rol
            usuario.save()
            lab_admin = LabAdmin(usuario=usuario)
            lab_admin.save()
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
    return render(request, 'lista_centros.html', {'object_list': centros})

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
    return render(request, 'lista_centros.html', {'object_list': centros, 'activated': False})