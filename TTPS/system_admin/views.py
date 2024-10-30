from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from medicos.models import Medico

class ListaMedicosView(ListView):
    model = Medico
    template_name = 'lista_medicos.html'

class CrearUsuarioView(CreateView):
    model = Medico
    template_name = 'system_admin/formulario_usuario.html'
    fields = ['username', 'first_name', 'last_name', 'fecha_nacimiento', 'email', 'rol']

class EditarUsuarioView(UpdateView):
    model = Medico
    template_name = 'system_admin/formulario_usuario.html'
    fields = ['username', 'first_name', 'last_name', 'fecha_nacimiento', 'email', 'rol']

#class ListaMedicosView(ListView):
#    model = Usuario
#    template_name = 'system_admin/lista_medicos.html'
#
#    def get_queryset(self):
#        # Filtrar solo los usuarios que tienen el rol de 'medico'
#        return Usuario.objects.filter(rol='medico')