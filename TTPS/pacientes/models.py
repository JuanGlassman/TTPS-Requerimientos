from django.db import models
from system_admin.models import Usuario
from django.core.validators import MinValueValidator

# Create your models here.

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    antecedentes = models.CharField(max_length=150, blank=True, null=True)
    historial_medico = models.CharField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

    class Meta:
        db_table = 'pacientes'

class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estudio = models.ForeignKey('estudios.Estudio', on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    numero = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Turno: {self.numero}"

    class Meta:
        db_table = 'turnos'