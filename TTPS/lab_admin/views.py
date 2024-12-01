import json
from django.shortcuts import render, get_object_or_404, redirect
import requests
from estudios.models import Estudio, EstadoEstudio
from estudios import views as estudio_estado
from .models import Presupuesto
from estudios import views as estudio_view
from transportista.views import agregar_estudio_a_pedido
from django.contrib.auth.decorators import login_required
from inicio_sesion.views import permission_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.core.paginator import Paginator
from django.db.models import Q
from TTPS.settings import EMAIL_HOST_PASSWORD

@login_required
@permission_required('lista_estudios_set')
def estudios(request):
    # Obtener parámetros de búsqueda y filtro
    search_query = request.GET.get('search', '').strip()
    selected_estado = request.GET.get('estado', '')
    order = request.GET.get('order', 'asc')  # Orden ascendente por defecto
    
    # Base de la consulta
    estudios_queryset = Estudio.objects.select_related('presupuesto').all()

    # Filtros de búsqueda y estado
    if search_query:
        estudios_queryset = estudios_queryset.filter(
            Q(id_interno__icontains=search_query)
        )
    if selected_estado:
        estudios_queryset = estudios_queryset.filter(estado=selected_estado)
    
    estudios_queryset = estudios_queryset.order_by(f"{'' if order == 'asc' else '-'}presupuesto__total")
    
    # Paginación
    paginator = Paginator(estudios_queryset, 10)  # 10 estudios por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "estudios.html", {
        "page_obj": page_obj,
        "search_query": search_query,
        "selected_estado": selected_estado,
        "order": order,
        "estados": EstadoEstudio,
    })



@login_required
@permission_required('presupuestar')
def form_presupuesto(request, estudio_id):
    estudio = get_object_or_404(Estudio, id_estudio=estudio_id)

    if (estudio.estado == EstadoEstudio.INICIADO):
        presupuesto = get_object_or_404(Presupuesto, estudio_id=estudio_id)
        return render(request, "editar_presupuesto.html", {
            "presupuesto": presupuesto,
            "estudio": estudio
        })
    else:
        #informar que no se puede presupuestar un estudio que no esta en estado iniciado
        return redirect('lab_admin:estudios')
    
def enviar_correo_presupuesto(email, context):
    """Envía un correo electrónico al paciente con el detalle del presupuesto."""
    try:
        subject = "Detalle del Presupuesto"
        body = render_to_string("detalle_presupuesto.html", context)

        message = Mail(
            from_email='laboratorios_laplata@hotmail.com', 
            to_emails=email,
            subject=subject,
            html_content=body
        )

        sg = SendGridAPIClient(EMAIL_HOST_PASSWORD)  
        response = sg.send(message)

        print(f"Correo enviado con código de estado: {response.status_code}")
        if response.body:
            print(f"Respuesta del servidor: {response.body}")

    except Exception as e:
        print(f"Error al enviar correo: {e}")

def guardar_presupuesto(exoma, genes, hallazgos, id_presupuesto):
    presupuesto = get_object_or_404(Presupuesto, id_presupuesto=id_presupuesto)    
    presupuesto.costo_exoma = exoma    
    presupuesto.costo_genes_extra = genes if genes != None else 0
    presupuesto.costo_hallazgos_secundarios = hallazgos if hallazgos != None else 0
    presupuesto.total = float(genes) + float(exoma) + (float(hallazgos) if hallazgos != None else 0)
    presupuesto.save()
    return presupuesto

@login_required
@permission_required('presupuestar')
def presupuestar(request):
    try:
        costo_exoma = request.POST.get('costo_exoma')
        costo_genes_extra = request.POST.get('costo_genes_extra')
        costo_hallazgos_secundario = request.POST.get('costo_hallazgos_secundarios')
        id_presupuesto = request.POST.get('id_presupuesto')
        id_estudio = request.POST.get('id_estudio')
        action = request.POST.get('action')

        if action == 'guardar':
            guardar_presupuesto(costo_exoma, costo_genes_extra, costo_hallazgos_secundario, int(id_presupuesto))
            messages.success(request, "El presupuesto se guardó de forma exitosa.")  
            return redirect("estudios:estudio_detalle", int(id_estudio))
        elif action == 'confirmar':
            presupuesto = guardar_presupuesto(costo_exoma, costo_genes_extra, costo_hallazgos_secundario, id_presupuesto)
            estudio = get_object_or_404(Estudio, id_estudio=presupuesto.estudio_id)
            
            res, estudio = estudio_view.estudio_presupuestado(estudio)
            
            if (res):
                estudio.save()
                messages.success(request, "El estudio se presupuestó de forma exitosa.") 
                #paciente_email = estudio.paciente.usuario.email
                paciente_email = "juanignacioglassman@gmail.com"
                context = {
                    'nombre_paciente':  estudio.paciente.usuario.first_name,
                    'costo_exoma': costo_exoma,
                    'costo_genes_extra': costo_genes_extra,
                    'costo_hallazgos_secundarios': costo_hallazgos_secundario,
                    'total': presupuesto.total,
                    'estudio': estudio
                }
                enviar_correo_presupuesto(paciente_email, context)
            return redirect("estudios:estudio_detalle", estudio.id_estudio) 
        
    except Exception as e:
        messages.warning(request, "Hubo un problema al configurar el presupuesto")
        return redirect('home')

@login_required
@permission_required('pagar_estudio')
def pagar_admin(request, estudio_id):
    try:
        estudio = get_object_or_404(Estudio, id_estudio=estudio_id)
        res, estudio = estudio_estado.estudio_pagado(estudio)
        estudio.save()    
        messages.success(request, "El estudio se pago de forma exitosa")
        return render(request, "estudio.html", {'estudio': estudio})
    
    except Exception as e:
        messages.warning(request, "Hubo un problema al pagar el estudio")
        return redirect('home')

@login_required
@permission_required('cancelar_estudio')
def cancelar_estudio(request, estudio_id):
    try:
        estudio = get_object_or_404(Estudio, id_estudio=estudio_id)
        res, estudio = estudio_estado.estudio_cancelado(estudio)
        estudio.save()
        messages.warning(request, f"El estudio {estudio.id_interno} se canceló de forma exitosa.")    
        return render(request, "estudio.html", {'estudio': estudio})
    except Exception as e:
        messages.warning(request, "Hubo un problema al cancelar el estudio.")
        return redirect('home')

@login_required
@permission_required('pedido_create')
@permission_required('pedido_update')
@permission_required('ruta_create')
@permission_required('ruta_update')
def realizar_estudio(request, estudio_id):
    try:
        estudio = get_object_or_404(Estudio, id_estudio=estudio_id)
        response = agregar_estudio_a_pedido(estudio_id)
        res, estudio = estudio_estado.estudio_realizado(estudio)
        estudio.save()
        messages.success(request, "El estudio tiene la muestra realizada.")
        return redirect("estudios:estudio_detalle", estudio.id_estudio) 
    
    except Exception as e:
        messages.warning(request, "Hubo un problema al realizar la muestra del estudio.")
        return redirect('home')

def enviar_correo_resultado(email, context):
    """Envía un correo electrónico al paciente con el detalle del resultado de un estudio utilizando SendGrid."""
    try:
        subject = "Detalle del Resultado"
        body = render_to_string("emails/detalle_resultado.html", context)

        message = Mail(
            from_email='laboratorios_laplata@hotmail.com',  
            to_emails=email,
            subject=subject,
            html_content=body
        )

        sg = SendGridAPIClient(EMAIL_HOST_PASSWORD)
        response = sg.send(message)

        print(f"Correo enviado con código de estado: {response.status_code}")
        if response.body:
            print(f"Respuesta del servidor: {response.body}")

    except Exception as e:
        print(f"Error al enviar correo: {e}")

    
@login_required
@permission_required('cargar_resultado')
def form_resultado(request, estudio_id):
    try:
        estudio = get_object_or_404(Estudio, id_estudio=estudio_id)
        variantes = get_variantes(estudio.patologia)
        return render(request, "resultado_estudio.html", { 
            "estudio": estudio, 
            "variantes": variantes
        })
    except Exception as e:
        messages.warning(request, "Hubo un problema para mostrar el formulario.")
        return redirect('home')

@login_required
@permission_required('cargar_resultado')
def cargar_resultado(request):
    try:
        id_estudio = request.POST.get('id_estudio')
        variantes = json.loads(request.POST.get('variantes', '[]'))
        estudio = get_object_or_404(Estudio, id_estudio=id_estudio)
        resultado = get_resultado(estudio, variantes) #buscar el resultado en backend
        estudio.resultado = resultado
        res, estudio = estudio_estado.estudio_finalizado(estudio)
        if (res):
            estudio.save()
            #paciente_email = estudio.paciente.usuario.email
            paciente_email = "juanignacioglassman@gmail.com"
            context = {
                'nombre_paciente': estudio.paciente.usuario.first_name,
                'resultado': resultado,
                'estudio': estudio,
            }
            enviar_correo_resultado(paciente_email, context)
        
        messages.success(request, "El resultado del estudio se cargó de forma existosa.")
        return redirect("estudios:estudio_detalle", estudio.id_estudio) 
    except Exception as e:
        messages.warning(request, "Hubo un problema al cargar el resultado del estudio.")
        return redirect('home')

def get_variantes(patologia):
    response = requests.get(f'https://api.claudioraverta.com/variantes/{patologia.gen}/', 
        headers={
            'Content-Type': 'application/json'
    })
                
    data = response.json()
    print(data)

    variantes = []
    for variante_data in data:
        variante = {
            'id': variante_data.get('id'),
            'nombre': variante_data.get('nombre')
        }
        variantes.append(variante)
    
    return variantes

def get_resultado(estudio, variantes):
    response = requests.post('https://api.claudioraverta.com/confirma-diagnostico/', 
        json={
            'patologia': estudio.patologia.nombre,
            'variantes': [s.get('nombre') for s in variantes ]
        },
        headers={
            'Content-Type': 'application/json'
    })
                
    data = response.json()
    print(data)
    print(data['valido'])
    if not data['valido']:
        return "negativo"
    return "positivo"
