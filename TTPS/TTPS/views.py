from django.shortcuts import render
from django.conf.urls import handler403


def permiso_denegado_view(request, exception):
    return render(request, 'error_403.html', status=403)

handler403 = permiso_denegado_view


def home(request):
    return render(request, 'home.html')
