from django.urls import path
from . import views

app_name = 'system_admin'

urlpatterns = [
    path('medicos/', views.ListaMedicosView.as_view(), name='lista_medicos'),
    #path('usuarios/crear/', views.CrearUsuarioView.as_view(), name='crear_usuario'),
    #path('usuarios/<int:pk>/editar/', views.EditarUsuarioView.as_view(), name='editar_usuario'),
]