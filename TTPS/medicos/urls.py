from django.contrib import admin
from django.urls import path, include
from . import views
from medicos import views as medico_view

app_name = 'medicos'

urlpatterns = [
    path("pacientes/", medico_view.pacientes, name="pacientes"),
    path("iniciar_estudio/", medico_view.iniciar_estudio, name="iniciar_estudio"),
    path("iniciar_estudio/<int:paciente_id>/", medico_view.iniciar_estudio_paciente, name="iniciar_estudio_paciente")
]