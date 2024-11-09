from django.urls import path
from . import views

app_name = 'system_admin'

urlpatterns = [
    path('usuarios/', views.ListaUsuariosView.as_view(), name='lista_usuarios'),
    path('usuarios/crear', views.CrearUsuarioView.as_view(), name='crear_usuario'),
    path('usuarios/<int:pk>/editar/', views.EditarUsuarioView.as_view(), name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/activar/<int:pk>', views.activar_usuario, name='activar_usuario'),
    path('usuarios/desactivados/', views.ListaUsuariosDesactivadosView.as_view(), name='usuarios_desactivados'),
    path('medicos/', views.ListaMedicosView.as_view(), name='lista_medicos'),
    path('medicos/crear', views.crear_medico_view, name='crear_medico'),
    path('medicos/desactivados/', views.ListaMedicosDesactivadosView.as_view(), name='medicos_desactivados'),
    path('medicos/<int:medico_id>/editar/', views.editar_medico_view, name='editar_medico'),
    path('labadmin/', views.ListaLabAdminsView.as_view(), name='lista_lab_admins'),
    path('labadmin/<int:id_lab_admin>/editar/', views.editar_lab_admin_view, name='editar_lab_admin'),
    path('labadmin/crear', views.crear_lab_admin_view, name='crear_lab_admin'),
    path('labadmin/desactivados/', views.ListaLabAdminsDesactivadosView.as_view(), name='lab_admin_desactivados'),
    path('centros/', views.ListaCentrosView.as_view(), name='lista_centros'),
    path('centros/crear', views.CrearCentroView.as_view(), name='crear_centro'),
    path('centros/<int:pk>/editar/', views.EditarCentroView.as_view(), name='editar_centro'),
    path('centros/eliminar/<int:pk>', views.eliminar_centro, name='eliminar_centro'),
]