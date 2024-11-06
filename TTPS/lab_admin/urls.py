from django.urls import path
from lab_admin import views as lab_admin_view

app_name = 'lab_admin'

urlpatterns = [
    path("", lab_admin_view.estudios, name="estudios"),
    path("pagar_admin/<int:estudio_id>/", lab_admin_view.pagar_admin, name="pagar_admin"),
]