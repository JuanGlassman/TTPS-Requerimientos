from django.db import models
from inicio_sesion.models import Usuario
from estudios.models import Estudio

# Create your models here.
class Presupuesto(models.Model):
    id_presupuesto = models.AutoField(primary_key=True)
    estudio = models.OneToOneField(Estudio, on_delete=models.PROTECT)
    costo_exoma = models.FloatField(null=True, default=0)
    costo_genes_extra = models.FloatField(null=True, default=0)

    def __str__(self):
        return f"Presupuesto #{self.id_presupuesto} - {self.estudio.id_interno}"

    class Meta:
        db_table = 'presupuestos'


class Centro(models.Model):
    id_centro = models.AutoField(primary_key=True)
    nombre = models.ForeignKey(Estudio, on_delete=models.PROTECT)

    def __str__(self):
        return f"Centro #{self.nombre}"

    class Meta:
        db_table = 'centro'

class LabAdmin(models.Model):
    id_lab_admin = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    centro_trabaja = models.OneToOneField(Centro, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.apellido}"

    class Meta:
        db_table = 'lab_admin'