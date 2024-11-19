from django.db import models
from inicio_sesion.models import Usuario
from estudios.models import Estudio
from django.core.validators import MinValueValidator

class Presupuesto(models.Model):
    id_presupuesto = models.AutoField(primary_key=True)
    estudio = models.OneToOneField(Estudio, on_delete=models.PROTECT)
    costo_exoma = models.FloatField(null=True, default=0)
    costo_genes_extra = models.FloatField(null=True, default=0)
    costo_hallazgos_secundarios = models.FloatField(null=True, default=0)
    total = models.FloatField(null=True, default=0)

    def __str__(self):
        return f"Presupuesto #{self.id_presupuesto} - {self.estudio.id_interno}"

    class Meta:
        db_table = 'presupuestos'


class Centro(models.Model):
    id_centro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)
    longitud = models.FloatField(null=True)
    latitud = models.FloatField(null=True)
    telefono = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Centro #{self.nombre}"

    class Meta:
        db_table = 'centro'

class LabAdmin(models.Model):
    id_lab_admin = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

    class Meta:
        db_table = 'lab_admin'

        
class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estudio = models.ForeignKey('estudios.Estudio', on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    horario = models.TimeField()  
    consentimiento = models.FileField(upload_to='consentimientos/', null=True, blank=True) 


    def __str__(self):
        return f"Turno: {self.numero}"

    class Meta:
        db_table = 'turnos'