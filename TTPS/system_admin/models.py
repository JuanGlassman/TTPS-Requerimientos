from django.db import models
from inicio_sesion.models import Usuario

class SystemAdmin(models.Model):
    id_system_admin = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.apellido}"

    class Meta:
        db_table = 'system_admin'