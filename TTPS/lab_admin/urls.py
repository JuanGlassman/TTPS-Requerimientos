from django.urls import path
from lab_admin import views as lab_admin_view

app_name = 'lab_admin'

urlpatterns = [
    path("estudios", lab_admin_view.estudios, name="estudios"),
    path("pagar_admin/<int:estudio_id>/", lab_admin_view.pagar_admin, name="pagar_admin"),
    path("form_presupuesto/<int:estudio_id>/", lab_admin_view.form_presupuesto, name="form_presupuesto"),
    path("presupuestar/", lab_admin_view.presupuestar, name="presupuestar"),
    path("cancelar/<int:estudio_id>/", lab_admin_view.cancelar_estudio, name="cancelar"),
    path("realizar/<int:estudio_id>/", lab_admin_view.realizar_estudio, name="realizar"),
    path("form_resultado/<int:estudio_id>/", lab_admin_view.form_resultado, name="form_resultado"),
    path("cargar_resultado/", lab_admin_view.cargar_resultado, name="cargar_resultado"),
    path("sample_set_list/", lab_admin_view.sample_set_list, name="sample_set_list"),
    path("sample_sets/<int:id_sample_set>/detalle/", lab_admin_view.sample_set_detalle, name="sample_set_detalle"),
    path("sample_sets/<int:id_sample_set>/enviar/", lab_admin_view.enviar_sample_set, name="enviar_sample_set"),
]