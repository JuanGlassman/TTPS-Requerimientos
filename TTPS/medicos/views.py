from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Medico
from inicio_sesion.models import Usuario
from estudios.models import Estudio
from pacientes.models import Paciente
from datetime import date

# Create your views here.
def estudios(request):
    estudios = Estudio.objects.order_by("fecha")
    return render(request, "medicos/estudios.html", { "estudios": estudios })

def pacientes(request):
    pacientes = Paciente.objects.order_by("id_paciente")
    return render(request, "medicos/pacientes.html", {"pacientes": pacientes})

def iniciar_estudio_paciente(request, paciente_id):        
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)    
    return render(request, "medicos/iniciar_estudio.html", {"paciente": paciente})

def iniciar_estudio(request):

    if request.method == "POST":
        try:
            # Obtener datos del formulario
            patologia = request.POST.get('patologia')
            tipo_estudio = request.POST.get('tipo_estudio')
            #sospecha = request.POST.get('sospecha')
            id_paciente = request.POST.get('id_paciente')
            #hallazgos_secundarios = request.POST.get('hallazgo') == 'on'
            
            # Generar id_interno (ajusta según tu lógica de negocio)
            nuevo_id = Estudio.objects.count() + 1
            id_interno = f"{nuevo_id}_{patologia[:3].upper()}"
            
            # Crear el estudio
            estudio = Estudio.objects.create(
                id_interno=id_interno,
                fecha=date.today(),
                tipo_estudio=tipo_estudio,
                patologia=patologia,
                paciente_id = id_paciente
                #estado=EstadoEstudio.INICIADO,
                # Si tienes un paciente en sesión o como parámetro:
                # paciente=paciente,
                # Otros campos según tu modelo
            )
            #estudio.save()  
        except Exception as e:
            return redirect('iniciar_estudio')
        
    return redirect("/medicos/estudios")