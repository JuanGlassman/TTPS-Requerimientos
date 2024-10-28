from django.db import models
from system_admin.models import Usuario

# Create your models here.

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    antecedentes = models.CharField(max_length=150, blank=True, null=True)
    historial_medico = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.apellido}"

    class Meta:
        db_table = 'pacientes'
