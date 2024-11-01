from django.urls import path
from . import views

app_name = 'system_admin'

urlpatterns = [
    path('usuarios/', views.ListaUsuariosView.as_view(), name='lista_usuarios'),
    path('usuarios/crear', views.CrearUsuarioView.as_view(), name='crear_usuario'),
    path('usuarios/<int:pk>/editar/', views.EditarUsuarioView.as_view(), name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>', views.eliminar_usuario, name='eliminar_usuario'),
]