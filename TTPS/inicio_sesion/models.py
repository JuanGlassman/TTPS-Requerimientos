from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


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
    

class Usuario(A):
    id_usuario = models.AutoField(primary_key=True)
    dni = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(
        max_length=1,
        choices=[('M', 'Masculino'), ('F', 'Femenino')],
        null=True,
        blank=True
    )
    rol = models.ForeignKey('Rol', on_delete=models.PROTECT, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Acceso al admin de Django
    is_superuser = models.BooleanField(default=False)  # Permisos de superusuario
    last_login = models.DateTimeField(null=True, blank=True)
    password = models.CharField(max_length=128)

    objects = UsuarioManager()  # Asigna el UserManager personalizado

    USERNAME_FIELD = "dni"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fecha_nacimiento']

    def set_password(self, raw_password):
        """Configura la contraseña del usuario."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Verifica la contraseña del usuario."""
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (DNI: {self.dni})"

    class Meta:
        db_table = 'usuarios'