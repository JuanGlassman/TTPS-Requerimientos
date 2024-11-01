from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from inicio_sesion.models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inicio_sesion.views import role_required

# TODO menu para activar un usuario
class ListaUsuariosDesactivadosView(ListView):
    model = Usuario
    template_name = 'lista_medicos.html'

    def get_queryset(self):
        return Usuario.objects.filter(is_deleted=True)

class ListaUsuariosView(ListView):
    model = Usuario
    template_name = 'lista_usuarios.html'
    
    def get_queryset(self):
        return Usuario.objects.filter(is_deleted=False)

class CrearUsuarioView(CreateView):
    model = Usuario
    template_name = 'formulario_usuario.html'
    fields = ['username', 'first_name', 'last_name', 'fecha_nacimiento', 'email', 'rol']

class EditarUsuarioView(UpdateView):
    model = Usuario
    template_name = 'formulario_usuario.html'
    fields = ['username', 'first_name', 'last_name', 'fecha_nacimiento', 'email', 'rol']

@login_required
@role_required(allowed_roles=['admin'])
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.is_deleted = True
        usuario.save()
        messages.success(request, "Usuario eliminado correctamente.")
        return redirect('system_admin:lista_usuarios')  # Redirigir a la lista de usuarios
    return render(request, 'system_admin/confirmar_eliminacion.html', {'usuario': usuario})
