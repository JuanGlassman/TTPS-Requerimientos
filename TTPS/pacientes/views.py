from pacientes.models import Paciente
from inicio_sesion.views import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from estudios.models import Estudio, EstadoEstudio
from django.core.paginator import Paginator

@login_required
def paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    return render(request, "paciente.html", {"paciente": paciente})

@login_required
@permission_required("historial_estudios_paciente")
def mis_estudios(request):
    estudios_list = Estudio.objects.order_by("fecha")
    paginator = Paginator(estudios_list, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "mis_estudios.html", {
        "page_obj": page_obj,
        "estados": EstadoEstudio
    })

