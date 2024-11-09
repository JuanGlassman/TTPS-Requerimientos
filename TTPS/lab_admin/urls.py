from django.urls import path
from lab_admin import views as lab_admin_view

app_name = 'lab_admin'

urlpatterns = [
    path("", lab_admin_view.estudios, name="estudios"),
    path("pagar_admin/<int:estudio_id>/", lab_admin_view.pagar_admin, name="pagar_admin"),
    path("form_presupuesto/<int:estudio_id>/", lab_admin_view.form_presupuesto, name="form_presupuesto"),
    path("presupuestar/", lab_admin_view.presupuestar, name="presupuestar"),
    path("cancelar/<int:estudio_id>/", lab_admin_view.cancelar_estudio, name="cancelar")
]