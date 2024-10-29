from django.db import models
from django.contrib.auth.models import AbstractUser


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
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
    genero = models.CharField(
        max_length=1,
        choices=Sexo.choices,
    )
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)

    # Heredados de AbstractUser: username, first_name, email, password
    
    class Meta:
        db_table = 'usuarios'