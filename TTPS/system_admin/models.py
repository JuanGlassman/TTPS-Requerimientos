from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

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

# Create your models here.
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

class SystemAdmin(models.Model):
    id_system_admin = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.apellido}"

    class Meta:
        db_table = 'system_admin'