from pacientes.models import Paciente
from inicio_sesion.views import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from estudios.models import Estudio, EstadoEstudio
from django.core.paginator import Paginator
from datetime import datetime, timedelta, time
from lab_admin.models import Turno, Centro
from .forms import TurnoForm
from django.http import JsonResponse
from django.contrib import messages
from django.http import FileResponse
import os
from TTPS.settings import BASE_DIR
from estudios.views import estudio_confirmado, estudio_autorizado

@login_required
def paciente_detalle(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    return render(request, "ver_detalle.html", {"paciente": paciente})

@login_required
@permission_required("historial_estudios_paciente")
def mis_estudios(request):
    paciente = request.user.paciente
    estudios_list = Estudio.objects.filter(paciente_id=paciente.id_paciente).order_by("fecha")
    paginator = Paginator(estudios_list, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "mis_estudios.html", {
        "page_obj": page_obj,
        "estados": EstadoEstudio
    })

@login_required
@permission_required("elegir_turno")
def sacar_turno(request, id_estudio):
    try:
        estudio = Estudio.objects.get(id_estudio=id_estudio)
    except Estudio.DoesNotExist:
        messages.error(request, "El estudio no existe.")
        return redirect('pacientes:mis_estudios')

    centros = Centro.objects.filter(is_deleted=False)
    horarios_disponibles = []

    if request.method == 'POST':
        centro_id = request.POST.get('centro')
        fecha = request.POST.get('fecha')
        horarios_disponibles = generar_horarios_disponibles(centro_id, fecha)

        form = TurnoForm(request.POST, request.FILES, horarios_disponibles=horarios_disponibles)
        if form.is_valid():
            try:
                turno = form.save(commit=False)
                turno.usuario = request.user
                turno.estudio = estudio
                turno.save()
                res, estudio = estudio_autorizado(estudio)
                if (res):
                    res, estudio = estudio_confirmado(estudio)
                if (res):
                    estudio.save()
                    messages.success(request, "Turno reservado correctamente.")
                return redirect('pacientes:confirmacion_turno', turno_id=turno.id_turno)
            except Exception as e:
                    messages.error(request, f"Error al crear el paciente: {e}")
        else:
            messages.error(request, f"Hubo un problema con el formulario: {form.errors.as_text()}")
    else:
        form = TurnoForm(horarios_disponibles=horarios_disponibles)

    return render(request, 'sacar_turno.html', {
        'form': form,
        'centros': centros,
        'estudio': estudio,
    })


def generar_horarios_disponibles(centro_id, fecha):
    """Genera los horarios disponibles para un centro y una fecha."""
    if not centro_id or not fecha:
        return []

    try:
        fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        centro = Centro.objects.get(id_centro=centro_id)

        horarios_totales = [
            (datetime.combine(fecha, time(hour=8)) + timedelta(minutes=15 * i)).time()
            for i in range(16)
        ]

        turnos_ocupados = Turno.objects.filter(centro=centro, fecha=fecha).values_list('horario', flat=True)
        horarios_disponibles = [h.strftime('%H:%M') for h in horarios_totales if h not in turnos_ocupados]

        return horarios_disponibles
    except (Centro.DoesNotExist, ValueError):
        return []




@permission_required("elegir_turno")
def obtener_horarios_disponibles(request):
    """Devuelve los horarios disponibles para un centro y fecha seleccionados."""
    fecha = request.GET.get('fecha')
    centro_id = request.GET.get('centro_id')

    if not fecha or not centro_id:
        return JsonResponse({'error': 'Parámetros faltantes: fecha y centro_id son requeridos.'}, status=400)

    # Llamar a la función con ambos parámetros
    horarios_disponibles = generar_horarios_disponibles(centro_id=centro_id, fecha=fecha)

    if horarios_disponibles:
        return JsonResponse({'horarios': horarios_disponibles})
    else:
        return JsonResponse({'error': 'No hay horarios disponibles o los datos proporcionados son inválidos.'}, status=400)



@login_required
@permission_required("elegir_turno")
def confirmacion_turno(request, turno_id):
    try:
        turno = Turno.objects.get(id_turno=turno_id, usuario=request.user)
        return render(request, 'confirmar_turno.html', {'turno': turno})
    except Turno.DoesNotExist:
        messages.error(request, "Turno no encontrado.")
        return redirect('pacientes:sacar_turno')


@login_required
@permission_required("dar_concentimiento")
def descargar_consentimiento(request):
    file_path = os.path.join(
        BASE_DIR, 
        'pacientes/static', 
        'CI.pdf'
    )
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf', as_attachment=True, filename='Consentimiento_Informado.pdf')
    else:
        messages.error(request, "El archivo no está disponible.")
        return redirect('pacientes:sacar_turno')