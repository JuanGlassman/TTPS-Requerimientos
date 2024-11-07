from django.shortcuts import render, get_object_or_404
from pacientes.models import Paciente

def paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    return render(request, "paciente.html", {"paciente": paciente})

