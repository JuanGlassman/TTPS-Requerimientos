"""
URL configuration for TTPS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from medicos import views as medico_view

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path("lab_admin/", include("lab_admin.urls")),
    path("medicos/", include("medicos.urls")),
    path("pacientes/", include("pacientes.urls")),
    path("system_admin/", include("system_admin.urls")),
    path("inicio_sesion/", include("inicio_sesion.urls")),
    path("estudios/", include('estudios.urls'))
]