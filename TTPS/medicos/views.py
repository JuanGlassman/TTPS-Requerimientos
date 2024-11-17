from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Medico
from inicio_sesion.models import Usuario
from estudios.models import Estudio
from lab_admin.models import Presupuesto
from pacientes.models import Paciente
from datetime import date
import requests, random, string
from estudios import views as estudio_views


def pacientes(request):
    pacientes = Paciente.objects.order_by("id_paciente")
    return render(request, "pacientes.html", {"pacientes": pacientes})

def iniciar_estudio_paciente(request, paciente_id):        
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)

    sintomas = get_sintomas()
    genes = get_genes()
    
    return render(request, "iniciar_estudio.html", {
        "paciente": paciente,
        "sintomas": sintomas,
        "genes": genes.get("results")
        })

def get_sintomas():
    response = requests.get('https://api.claudioraverta.com/lista-sintomas/?page=1&page_size=15')
    if response.status_code == 200:
        data = response.json()
    return data

def get_genes():
    response = requests.get('https://api.claudioraverta.com/lista-genes/?page=1&page_size=15')
    if response.status_code == 200:
        data = response.json()
    return data

# def get_gener_analizar():
#     response = requests.get('https://api.claudioraverta.com/genes-analizar/Pompe/')
    # print(f"{response.status_code}")
    # if response.status_code == 200:
    #     data = response.json()
    #     return render(request, "iniciar_estudio.html", {
    #         "paciente": paciente,
    #         "api_data": data
    #     })

    # else:
    #     # Manejar error de la API
    #     return render(request, "iniciar_estudio.html", {
    #         "paciente": paciente,
    #         "error": f"Error API: {response.status_code}"
    #     })

def iniciar_estudio(request):    
    try:            
        patologia = request.POST.get('patologia')
        tipo_estudio = request.POST.get('tipo_estudio')
        sintomas = request.POST.getlist('sintomas')
        sospecha = request.POST.get('sospecha')
        id_paciente = request.POST.get('id_paciente')
        print( request.POST.get('hallazgo'))
        hallazgos_secundarios = request.POST.get('hallazgo') == 'on'
        genes = request.POST.getlist('genes')
        paciente = get_object_or_404(Paciente, id_paciente=id_paciente)

        #Cuando esté lo del logeo y roles implemento lo del medico
        #medico = get_object_or_404(Medico, usuario_id=request.user.id)
        
        #Crear el estudio
        estudio = Estudio.objects.create(
            id_interno = generar_id_interno(paciente),
            fecha=date.today(),
            tipo_estudio=tipo_estudio,
            patologia=patologia,
            paciente_id = id_paciente,
            medico_id = 1, #medico.id_medico
            tipo_sospecha = int(sospecha),
            hallazgos_secundarios = hallazgos_secundarios
        ) 
        
        estudio_views.estudio_iniciado(estudio)
        print(hallazgos_secundarios)
        presupuesto = Presupuesto.objects.create(
            estudio_id = estudio.id_estudio,
            costo_exoma = 500.0,
            costo_genes_extra = len(genes) * 30,
            costo_hallazgos_secundarios = 200.0 if hallazgos_secundarios else 0
        )
        
        return redirect("/lab_admin")
            
    except Exception as e:
        print(e)
        return redirect('iniciar_estudio')
    

def generar_id_interno(paciente) -> str:
    num_aleatorio = ''.join(random.choices(string.digits, k=4))

    apellido = paciente.usuario.last_name
    nombre = paciente.usuario.first_name
    
    # Si el apellido/nombre es menor a 3 letras, se rellena con X
    apellido_parte = (apellido[:3] if len(apellido) >= 3 else apellido + 'X' * (3 - len(apellido))).upper()
    nombre_parte = (nombre[:3] if len(nombre) >= 3 else nombre + 'X' * (3 - len(nombre))).upper()
    
    # Construir el ID interno
    id_interno = f"{num_aleatorio}_{apellido_parte}_{nombre_parte}"
    
    return id_interno