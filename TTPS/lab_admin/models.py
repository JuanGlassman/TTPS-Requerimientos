from django.db import models
from system_admin.models import Usuario
from estudios.models import Estudio
from django.core.validators import MinValueValidator

# Create your models here.
class Presupuesto(models.Model):
    id_presupuesto = models.AutoField(primary_key=True)
    estudio = models.OneToOneField(Estudio, on_delete=models.PROTECT)

    def __str__(self):
        return f"Presupuesto #{self.id_presupuesto} - {self.estudio.id_interno}"

    class Meta:
        db_table = 'presupuestos'


class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    numero = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Turno: {self.numero}"

    class Meta:
        db_table = 'turno'

class Centro(models.Model):
    id_centro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"Centro #{self.nombre}"

    class Meta:
        db_table = 'centro'

class LabAdmin(models.Model):
    id_lab_admin = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    centro_trabaja = models.OneToOneField(Centro, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

    class Meta:
        db_table = 'lab_admin'