from django.db import models
from pacientes.models import Paciente
from django.core.validators import MinValueValidator

class SampleSet(models.Model):
    id_sample_set = models.AutoField(primary_key=True)
    cantidad_muestras = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_envio = models.DateField(null=True, blank=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Sample Set #{self.id_sample_set}"

    class Meta:
        db_table = 'sample_sets'

class Enfermedad(models.Model):
    id_enfermedad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50) 

    def __str__(self):
        return f"Enfermedad #{self.nombre}"

    class Meta:
        db_table = 'enfermedad'


# Create your models here.
class EstadoEstudio(models.TextChoices):
    INICIADO = 'IN', 'Iniciado'
    PRESUPUESTADO = 'PR', 'Presupuestado'
    PAGADO = 'PA', 'Pagado'
    TURNO_CONFIRMADO = 'TC', 'Turno Confirmado'
    REALIZADA = 'RE', 'Realizada'
    CENTRALIZADA = 'CE', 'Centralizada'
    ENVIADA_EXTERIOR = 'EE', 'Enviada al Exterior'
    FINALIZADO = 'FI', 'Finalizado'
    
class Estudio(models.Model):
    id_estudio = models.AutoField(primary_key=True)
    id_interno = models.CharField(max_length=50)  # Formato: "1234_APE_NOM"
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    fecha = models.DateField()
    tipo_estudio = models.CharField(max_length=100)
    resultado = models.TextField()
    estado = models.CharField(
        max_length=2,
        choices=EstadoEstudio.choices,
        default=EstadoEstudio.INICIADO,
    )
    sample_set = models.ForeignKey(SampleSet, on_delete=models.PROTECT, null=True, blank=True)
    patologia = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id_interno} - {self.paciente}"

    class Meta:
        db_table = 'estudios'