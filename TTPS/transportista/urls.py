from django.urls import path
from transportista import views as transportista_view

app_name = 'transportista'

urlpatterns = [
    path("lista_pedidos/", transportista_view.lista_pedidos, name="lista_pedidos"),
    path("agregar_estudio_a_pedido/<int:estudio_id>/", transportista_view.agregar_estudio_a_pedido, name="agregar_estudio_a_pedido"),
    path("mapa/<int:hoja_id>", transportista_view.ver_mapa, name="ver_mapa"),
    path("pedido/<int:pedido_id>/", transportista_view.ver_pedido, name="ver_pedido"),
    path("iniciar_recorrido/<int:hoja_id>/", transportista_view.iniciar_recorrido, name="iniciar_recorrido"),
    path("finalizar_recorrido/<int:hoja_id>/", transportista_view.finalizar_recorrido, name="finalizar_recorrido"),
    path("entregar_pedido/", transportista_view.entregar_pedido, name="entregar_pedido"),
    path("cancelar_pedido/<int:pedido_id>/", transportista_view.cancelar_pedido, name="cancelar_pedido"),
]