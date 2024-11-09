from django.urls import path
from . import views

app_name = 'inicio_sesion'


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'), 
    path('cambiar_contrasena/', views.cambiar_contrasena_view, name='cambiar_contrasena'),  
    path('editar/', views.editar_perfil, name='editar'), 
]
