from django.urls import path
from transportista import views as transportista_view

app_name = 'lab_admin'

urlpatterns = [
    path("lista_pedidos", transportista_view.lista_pedidos, name="lista_pedidos")
]