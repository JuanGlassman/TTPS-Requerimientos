from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'roles'

class Sexo(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMENINO = 'F', 'Femenino'
    OTRO = 'O', 'Otro'
    
class Usuario(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    dni = models.IntegerField(unique=True, null=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(
        max_length=1,
        choices=[('M', 'Masculino'), ('F', 'Femenino')],
        null=True,
        blank=True
    )
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    
    class Meta:
        db_table = 'usuarios'