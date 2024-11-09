from django.urls import path
from pacientes import views as paciente_view

app_name = 'pacientes'

urlpatterns = [
    path("<int:paciente_id>/", paciente_view.paciente, name="paciente_detalle")
]