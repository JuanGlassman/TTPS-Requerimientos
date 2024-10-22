from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from enum import Enum

class Genero(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMENINO = 'F', 'Femenino'
    OTRO = 'O', 'Otro'

class EstadoEstudio(models.TextChoices):
    INICIADO = 'IN', 'Iniciado'
    PRESUPUESTADO = 'PR', 'Presupuestado'
    PAGADO = 'PA', 'Pagado'
    TURNO_CONFIRMADO = 'TC', 'Turno Confirmado'
    REALIZADA = 'RE', 'Realizada'
    CENTRALIZADA = 'CE', 'Centralizada'
    ENVIADA_EXTERIOR = 'EE', 'Enviada al Exterior'
    FINALIZADO = 'FI', 'Finalizado'

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'roles'

class Usuario(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    apellido = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(
        max_length=1,
        choices=Genero.choices,
    )
    matricula = models.CharField(max_length=50, blank=True, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)

    # Heredados de AbstractUser: username, first_name, email, password
    
    class Meta:
        db_table = 'usuarios'

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(
        max_length=1,
        choices=Genero.choices,
    )

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.apellido}"

    class Meta:
        db_table = 'pacientes'

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    numero_licencia = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr. {self.usuario.first_name} {self.usuario.apellido}"

    class Meta:
        db_table = 'medicos'

class SampleSet(models.Model):
    id_sample_set = models.AutoField(primary_key=True)
    cantidad_muestras = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_envio = models.DateField(null=True, blank=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Sample Set #{self.id_sample_set}"

    class Meta:
        db_table = 'sample_sets'

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

class Presupuesto(models.Model):
    id_presupuesto = models.AutoField(primary_key=True)
    estudio = models.OneToOneField(Estudio, on_delete=models.PROTECT)
    # Chusmear bien esta parte del modelo. Por el tema de la edición, etc.

    def __str__(self):
        return f"Presupuesto #{self.id_presupuesto} - {self.estudio.id_interno}"

    class Meta:
        db_table = 'presupuestos'