import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Medico
from estudios.models import Estudio, EstadoEstudio
from django.core.paginator import Paginator
from estudios.models import Estudio, Enfermedad, Sintoma, Gen, Lugar
from lab_admin.models import Presupuesto
from pacientes.models import Paciente
from datetime import date
import requests, random, string, secrets
from estudios import views as estudio_views
from .validaciones import validar_inicio_estudio
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from inicio_sesion.views import permission_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from pacientes.models import Paciente
from .forms import PacienteForm
from django.core.paginator import Paginator
from django.db.models import Q

from system_admin.views import enviar_correo_nuevo_usuario

from system_admin.forms import UsuarioForm
from inicio_sesion.models import Usuario, Rol

@login_required
@permission_required('lista_pacientes')
def pacientes(request):
    # Obtener parámetros de búsqueda
    search_query = request.GET.get('search', '')

    # Filtrar pacientes por nombre o apellido
    pacientes = Paciente.objects.filter(
        Q(usuario__first_name__icontains=search_query) | Q(usuario__last_name__icontains=search_query)
    ).order_by("id_paciente")

    # Paginar los resultados
    paginator = Paginator(pacientes, 10)  # Mostrar 10 pacientes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "pacientes.html", {
        "page_obj": page_obj,
        "search_query": search_query,
    })


@login_required
@permission_required('iniciar_estudio')
def iniciar_estudio_paciente(request, paciente_id):        
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)

    genes = get_genes()
    
    lugares = Lugar.objects.all()
    
    return render(request, "iniciar_estudio.html", {
        "paciente": paciente,
        "patologias": get_patologias(),
        "genes": genes.get("results"),
        "lugares": lugares,
        })

def get_patologias():
    return Enfermedad.objects.order_by()

def get_genes():
    response = requests.get('https://api.claudioraverta.com/lista-genes/?page=1&page_size=15')
    if response.status_code == 200:
        data = response.json()
    return data

@login_required
@permission_required('iniciar_estudio')
def iniciar_estudio(request):    
    try:   
        sintomas = json.loads(request.POST.get('sintomas', '[]'))
        print(sintomas)
        patologia = request.POST.get('patologia')
        tipo_estudio = request.POST.get('tipo_estudio')
        sospecha = request.POST.get('sospecha')
        parentesco = request.POST.get('parentesco')
        id_paciente = request.POST.get('id_paciente')
        hallazgos_secundarios = request.POST.get('hallazgo') == 'on'
        genes = request.POST.getlist('genes')
        paciente = get_object_or_404(Paciente, id_paciente=id_paciente)

        if not validar_inicio_estudio(request):
            messages.warning(request, "Hubo problemas para validar el formulario. Intente de nuevo.")
            return redirect('medicos:iniciar_estudio_paciente', int(id_paciente))
        
        medico = get_object_or_404(Medico, usuario_id=request.user)        

        
        estudio = Estudio.objects.create(
            id_interno = generar_id_interno(paciente),
            fecha=date.today(),
            tipo_estudio=tipo_estudio,
            patologia_id = patologia,
            paciente_id = id_paciente,
            medico_id = medico.id_medico,
            tipo_sospecha = int(sospecha),            
            hallazgos_secundarios = hallazgos_secundarios,
            parentesco = parentesco
        )

        # #Asignar los sintomas. Si no existen, se dan de alta.
        for sintoma in sintomas:
            try:
                sintomaAux = Sintoma.objects.get(id_sintoma_api=sintoma.get('id'))
                print(sintomaAux)
                estudio.sintomas.add(sintomaAux)          
            except:
                sintomaNuevo = Sintoma.objects.create(
                    id_sintoma_api = sintoma.get('id'),
                    nombre = sintoma.get('nombre')
                )
                estudio.sintomas.add(sintomaNuevo)

        # #Asignar los genes. Si no existen, se dan de alta.
        if(not genes):
            for gen in genes:
                try:
                    genAux = Gen.objects.get(id_gen_api=gen.get('id'))
                    print(genAux)
                    estudio.genes.add(sintomaAux)          
                except:
                    genNuevo = Gen.objects.create(
                        id_gen_api = gen.get('id'),
                        nombre = gen.get('nombre')
                    )
                    estudio.genes.add(sintomaNuevo)
        
        estudio_views.estudio_iniciado(estudio)
        
        presupuesto = Presupuesto.objects.create(
            estudio_id = estudio.id_estudio,
            costo_exoma = 500.0,
            costo_genes_extra = len(genes) * 30,
            costo_hallazgos_secundarios = 200.0 if hallazgos_secundarios else 0,
            total = 500.0 + len(genes) * 30 + (200.0 if hallazgos_secundarios else 0)
        )
        
        messages.success(request, "El estudio se ha iniciado con éxito.")
        return redirect("estudios:estudio_detalle", estudio.id_estudio)
            
    except Exception as e:
        messages.warning("Error al iniciar estudio. Intente de nuevo.")
        return redirect('home')
    
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

@login_required
@permission_required("historial_estudios_paciente")
def estudios_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    estudios_list = Estudio.objects.filter(paciente_id=paciente.id_paciente).order_by("fecha")
    paginator = Paginator(estudios_list, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "estudios_paciente.html", {
        "page_obj": page_obj,
        "estados": EstadoEstudio,
        "paciente": paciente
    })

@login_required
@permission_required('paciente_create')
def crear_paciente(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        paciente_form = PacienteForm(request.POST)

        if usuario_form.is_valid() and paciente_form.is_valid():
            try:
                rol_paciente = Rol.objects.get(nombre='paciente') 
                usuario, password = usuario_form.save(commit=False, rol=rol_paciente)
                caracteres = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(secrets.choice(caracteres) for _ in range(12))
                usuario.set_password(password)
                usuario.save()

                # Crear el paciente asociado al usuario
                paciente = Paciente(
                    usuario=usuario,
                    antecedentes=paciente_form.cleaned_data['antecedentes'],
                    historial_medico=paciente_form.cleaned_data['historial_medico']
                )
                paciente.save()
                
                enviar_correo_nuevo_usuario(usuario, password)
                messages.success(request, "Paciente creado exitosamente.")
                return redirect('medicos:listar_pacientes') 
            except Exception as e:
                messages.error(request, f"Error al crear el paciente: {e}")
        else:
            messages.error(request, "Formulario inválido. Por favor, verifica los datos ingresados.")
    else:
        usuario_form = UsuarioForm()
        paciente_form = PacienteForm()

    return render(request, 'form_paciente.html', {
        'usuario_form': usuario_form,
        'paciente_form': paciente_form,
        'titulo': 'Crear Paciente',
        'boton': 'Guardar Paciente',
    })



@login_required
@permission_required('paciente_update')
def editar_paciente(request, id_paciente):
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    usuario = paciente.usuario 

    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST, instance=usuario)
        paciente_form = PacienteForm(request.POST, instance=paciente)

        if usuario_form.is_valid() and paciente_form.is_valid():
            try:
                usuario_form.save()
                paciente_form.save()

                messages.success(request, "Paciente editado exitosamente.")
                return redirect('medicos:listar_pacientes')
            except Exception as e:
                messages.error(request, f"Error al editar el paciente: {e}")
        else:
            messages.error(request, "Formulario inválido. Por favor, verifica los datos ingresados.")
    else:
        usuario_form = UsuarioForm(instance=usuario)
        paciente_form = PacienteForm(instance=paciente)

    return render(request, 'form_paciente.html', {
        'usuario_form': usuario_form,
        'paciente_form': paciente_form,
        'titulo': 'Editar Paciente',
        'boton': 'Guardar Cambios',
    })