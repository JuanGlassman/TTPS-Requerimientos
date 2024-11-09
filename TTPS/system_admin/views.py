from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django import forms
from inicio_sesion.models import Usuario
from medicos.models import Medico
from lab_admin.models import LabAdmin
from lab_admin.models import Centro
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inicio_sesion.views import role_required


class UsuarioForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d']
    )
    
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'fecha_nacimiento', 'email', 'rol']

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['especialidad', 'matricula']

class LabAdminForm(forms.ModelForm):
    class Meta:
        model = LabAdmin
        fields = ['centro_trabaja']

class ListaUsuariosDesactivadosView(ListView):
    model = Usuario
    template_name = 'lista_usuarios.html'

    def get_queryset(self):
        return Usuario.objects.filter(is_deleted=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activated'] = False
        return context

class ListaUsuariosView(ListView):
    model = Usuario
    template_name = 'lista_usuarios.html'
    
    def get_queryset(self):
        return Usuario.objects.filter(is_deleted=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activated'] = True
        return context

class CrearUsuarioView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'formulario_usuario.html'

    def get_success_url(self):
        return reverse_lazy('system_admin:lista_usuarios')

class EditarUsuarioView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'formulario_usuario.html'

    def get_success_url(self):
        return reverse_lazy('system_admin:lista_usuarios')

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.is_deleted = True
    usuario.save()
    messages.success(request, "Usuario eliminado correctamente.")
    return redirect('system_admin:lista_usuarios')

def activar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.is_deleted = False
    usuario.save()
    messages.success(request, "Usuario activado correctamente.")
    return redirect('system_admin:usuarios_desactivados')

class ListaMedicosView(ListView):
    model = Medico
    template_name = 'lista_medicos.html'

    def get_queryset(self):
        return Medico.objects.filter(usuario__is_deleted=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activated'] = True
        return context
    
class ListaMedicosDesactivadosView(ListView):
    model = Medico
    template_name = 'lista_medicos.html'

    def get_queryset(self):
        return Medico.objects.filter(usuario__is_deleted=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activated'] = False
        return context
    
def crear_medico_view(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        medico_form = MedicoForm(request.POST)

        if usuario_form.is_valid() and medico_form.is_valid():
            usuario = usuario_form.save()
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

class ListaLabAdminsView(ListView):
    model = LabAdmin
    template_name = 'lista_lab_admins.html'

    def get_queryset(self):
        return LabAdmin.objects.filter(usuario__is_deleted=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activated'] = True
        return context
    
class ListaLabAdminsDesactivadosView(ListView):
    model = LabAdmin
    template_name = 'lista_lab_admins.html'

    def get_queryset(self):
        return LabAdmin.objects.filter(usuario__is_deleted=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activated'] = False
        return context

def crear_lab_admin_view(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        lab_admin_form = LabAdminForm(request.POST)

        if usuario_form.is_valid() and lab_admin_form.is_valid():
            usuario = usuario_form.save()
            lab_admin = lab_admin_form.save(commit=False)
            lab_admin.usuario = usuario
            lab_admin.save()
            return redirect('system_admin:lista_lab_admins')

    else:
        usuario_form = UsuarioForm()
        lab_admin_form = LabAdminForm()

    context = {
        'usuario_form': usuario_form,
        'lab_admin_form': lab_admin_form,
    }
    return render(request, 'crear_lab_admin.html', context)

def editar_lab_admin_view(request, id_lab_admin):
    lab_admin = get_object_or_404(LabAdmin, pk=id_lab_admin)
    usuario_form = UsuarioForm(request.POST or None, instance=lab_admin.usuario)
    lab_admin_form = LabAdminForm(request.POST or None, instance=lab_admin)

    if request.method == 'POST':
        if usuario_form.is_valid() and lab_admin_form.is_valid():
            usuario_form.save()
            lab_admin_form.save()
            return redirect('system_admin:lista_lab_admins')

    context = {
        'usuario_form': usuario_form,
        'lab_admin_form': lab_admin_form,
        'lab_admin': lab_admin,
    }

    return render(request, 'editar_lab_admin.html', context)

class ListaCentrosView(ListView):
    model = Centro
    template_name = 'lista_centros.html'
    
    def get_queryset(self):
        return Centro.objects.filter()

class CrearCentroView(CreateView):
    model = Centro
    fields = ['nombre']
    template_name = 'formulario_centro.html'

    def get_success_url(self):
        return reverse_lazy('system_admin:lista_centros')

class EditarCentroView(UpdateView):
    model = Centro
    fields = ['nombre']
    template_name = 'formulario_centro.html'

    def get_success_url(self):
        return reverse_lazy('system_admin:lista_centros')

def eliminar_centro(request, pk):
    centro = get_object_or_404(Centro, pk=pk)
    centro.delete()
    messages.success(request, "Centro eliminado correctamente.")
    return redirect('system_admin:lista_centros')