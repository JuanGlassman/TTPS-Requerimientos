import http
import json

import requests

def validar_inicio_estudio(request):
    sintomas = json.loads(request.POST.get('sintomas', '[]'))
    print("ENTRO A VALIDAR")
    if not validar_sintomas(sintomas): return False
    
    if not validar_patologia(request.POST.get('patologia')): return False
    if not validar_sospecha(request.POST.get('sospecha'), request.POST.get('parentesco')): return False
    print("PASO LAS PRIMERAS VALIDACIONES")
    if request.POST.get('sospecha') == '1':
        if not validar_sintomas_con_patologia(request.POST.get('patologia_nombre'), sintomas): return False
    return True

def validar_sintomas(sintomas):
    print(sintomas)
    if not sintomas:
        return False
    return True

def validar_patologia(patologia):
        if not patologia:
            return False
        return True

def validar_sospecha(sospecha, parentesco):
    if sospecha != '1' and not parentesco:
        return False
    return True

def validar_sintomas_con_patologia(patologia, sintomas):
    print(patologia)
    response = requests.post('https://api.claudioraverta.com/sintomas-validos/', 
        json={
            'patologia': patologia,
            'sintomas': [s.get('nombre') for s in sintomas]
        },
        headers={
            'Content-Type': 'application/json'
    })
                
    data = response.json()
    print(data)
    print(data['valido'])
    if not data['valido']:
        return False
    return True