from django.db import models
from pacientes.models import Paciente
from medicos.models import Medico
from django.core.validators import MinValueValidator
from django.utils import timezone
from datetime import datetime
from django.utils.timezone import is_naive, make_aware, now

class SampleSet(models.Model):
    id_sample_set = models.AutoField(primary_key=True)
    fecha_envio = models.DateField(null=True, blank=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    estudios = models.ManyToManyField('Estudio', blank=True)
    archivo_pdf = models.FileField(upload_to='sample_sets/', null=True, blank=True)

    def __str__(self):
        return f"Sample Set #{self.id_sample_set}"

    class Meta:
        db_table = 'sample_sets'

class Enfermedad(models.Model):
    id_enfermedad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    gen = models.CharField(max_length=15)

    def __str__(self):
        return f"Enfermedad #{self.nombre}"

    class Meta:
        db_table = 'enfermedad'


class Gen(models.Model):
    id = models.AutoField(primary_key=True)
    id_gen_api = models.IntegerField()
    nombre = models.CharField(max_length=20)

    class Meta:
        db_table = 'genes'

    def __str__(self):
        return self.nombre
    
class Sintoma(models.Model):
    id = models.AutoField(primary_key=True)
    id_sintoma_api = models.IntegerField()
    nombre = models.CharField(max_length=20)

    class Meta:
        db_table = 'sintomas'

    def __str__(self):
        return self.nombre

class EstadoEstudio(models.TextChoices):
    INICIADO = 'Iniciado'
    PRESUPUESTADO = 'Presupuestado'
    PAGADO = 'Pagado'
    AUTORIZADO = 'Autorizado'
    TURNO_CONFIRMADO = 'Turno Confirmado'
    REALIZADA = 'Realizada'
    CENTRALIZADA = 'Centralizada'
    ENVIADA_EXTERIOR = 'Enviada al Exterior'
    FINALIZADO = 'Finalizado'
    CANCELADO = 'Cancelado'

class Lugar(models.Model):
    lugar_id = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=100, blank=True)
    provincia = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ciudad}, {self.provincia}, {self.pais}"

    class Meta:
        db_table = 'lugares'
        unique_together = ('ciudad', 'provincia', 'pais') 

class Estudio(models.Model):
    id_estudio = models.AutoField(primary_key=True)
    id_interno = models.CharField(max_length=50)  # Formato: "1234_APE_NOM"
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    fecha = models.DateField()
    tipo_estudio = models.CharField(max_length=100)
    resultado = models.TextField(null=True)
    estado = models.CharField(  
        max_length=20,
        choices=EstadoEstudio.choices,
        default=EstadoEstudio.INICIADO,
    )
    hallazgos_secundarios = models.BooleanField(default=False)
    tipo_sospecha = models.IntegerField()
    parentesco = models.CharField(max_length=30, null=True)
    sample_set = models.ForeignKey(SampleSet, on_delete=models.PROTECT, null=True, blank=True)
    patologia = models.ForeignKey(Enfermedad, on_delete=models.PROTECT, null=True )
    genes = models.ManyToManyField(Gen)
    sintomas = models.ManyToManyField(Sintoma)
    lugar = models.ForeignKey(Lugar, on_delete=models.PROTECT, null=True) 

    def __str__(self):
        return f"{self.id_interno} - {self.paciente}"

    class Meta:
        db_table = 'estudios'

class HistorialEstudio(models.Model):
    id_historial_estudio = models.AutoField(primary_key=True)
    estudio = models.ForeignKey(Estudio, on_delete=models.PROTECT)
    estado = models.CharField(  
        max_length=20,
        choices=EstadoEstudio.choices,
        null=False
    )
    fecha_inicio = models.DateTimeField(null=False, default=timezone.now)
    fecha_fin = models.DateTimeField(null=True)

    @property
    def tiempo_en_estado(self):
        """
        Calcula el tiempo que el estudio estuvo en un estado.
        Si no tiene fecha_fin, calcula el tiempo desde fecha_inicio hasta ahora.
        """
        inicio = self.fecha_inicio
        fin = self.fecha_fin or now()

        # Asegurarse de que ambas fechas sean aware
        if is_naive(inicio):
            inicio = make_aware(inicio)
        if is_naive(fin):
            fin = make_aware(fin)

        return fin - inicio