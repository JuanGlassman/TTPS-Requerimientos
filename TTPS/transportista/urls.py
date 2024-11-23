from django.urls import path
from transportista import views as transportista_view

app_name = 'transportista'

urlpatterns = [
    path("lista_pedidos/", transportista_view.lista_pedidos, name="lista_pedidos"),
    path("agregar_estudio_a_pedido/<int:estudio_id>/", transportista_view.agregar_estudio_a_pedido, name="agregar_estudio_a_pedido"),
]