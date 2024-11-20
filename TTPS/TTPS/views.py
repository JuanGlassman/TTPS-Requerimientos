from django.shortcuts import render

def acceso_denegado_view(request, exception=None):
    return render(request, 'error_403.html', status=403)



def home(request):
    return render(request, 'home.html')
