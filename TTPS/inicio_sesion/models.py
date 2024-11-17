from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, dni, password=None, **extra_fields):
        """Crea y guarda un usuario con el dni especificado."""
        if not dni:
            raise ValueError("El usuario debe tener un DNI")
        user = self.model(dni=dni, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, password=None, **extra_fields):
        """Crea y guarda un superusuario con el dni especificado."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(dni, password, **extra_fields)

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
    dni = models.IntegerField(unique=True, null=False)
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
    first_login = models.BooleanField(default=True)

    objects = UsuarioManager()  # Asigna el UserManager personalizado

    USERNAME_FIELD = "dni"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fecha_nacimiento']

    def __str__(self):
        return f"{self.first_name} {self.last_name})"

    class Meta:
        db_table = 'usuarios'