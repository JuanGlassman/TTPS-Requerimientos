from django.urls import path
from estudios import views as estudio_view

app_name = 'estudios'

urlpatterns = [
    path("<int:estudio_id>/", estudio_view.estudio, name="estudio_detalle"),
    path('historial/<int:id_estudio>/', estudio_view.historial_estudio_view, name='historial_estudio'),
]