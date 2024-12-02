from django.urls import path
from . import views

app_name = 'system_admin'

urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/activar/<int:pk>', views.activar_usuario, name='activar_usuario'),
    path('usuarios/desactivados/', views.lista_usuarios_desactivados, name='usuarios_desactivados'),
    path('medicos/', views.lista_medicos, name='lista_medicos'),
    path('medicos/crear', views.crear_medico_view, name='crear_medico'),
    path('medicos/desactivados/', views.lista_medicos_desactivados, name='medicos_desactivados'),
    path('medicos/<int:medico_id>/editar/', views.editar_medico_view, name='editar_medico'),
    path('labadmin/', views.lista_lab_admins, name='lista_lab_admins'),
    path('labadmin/<int:id_lab_admin>/editar/', views.editar_lab_admin_view, name='editar_lab_admin'),
    path('labadmin/crear', views.crear_lab_admin_view, name='crear_lab_admin'),
    path('labadmin/desactivados/', views.lista_lab_admins_desactivados, name='lab_admin_desactivados'),
    path('centros/', views.lista_centros, name='lista_centros'),
    path('centros/crear', views.crear_centro, name='crear_centro'),
    path('centros/<int:pk>/editar/', views.editar_centro, name='editar_centro'),
    path('centros/eliminar/<int:pk>', views.eliminar_centro, name='eliminar_centro'),
    path('centros/desactivados/', views.lista_centros_desactivados, name='centros_desactivados'),
    path('centros/activar/<int:pk>', views.activar_centro, name='activar_centro'),
]