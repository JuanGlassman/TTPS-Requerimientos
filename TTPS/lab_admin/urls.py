from django.urls import path
from lab_admin import views as lab_admin_view

app_name = 'lab_admin'

urlpatterns = [
    path("estudios/", lab_admin_view.estudios, name="estudios"),
]