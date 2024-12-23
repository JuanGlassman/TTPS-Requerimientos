from django.db import models
from inicio_sesion.models import Usuario 

# Create your models here.
class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self):
        return f"Dr. {self.usuario.first_name} {self.usuario.last_name}"

    class Meta:
        db_table = 'medicos'