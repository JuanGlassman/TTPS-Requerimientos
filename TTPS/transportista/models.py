from django.db import models
from django.core.validators import MinValueValidator
from inicio_sesion.models import Usuario
from estudios.models import Estudio
from lab_admin.models import Centro

class Transportista(models.Model):
    id_transportista = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

    class Meta:
        db_table = 'transportista'

# estados del pedido: pendiente, finalizado
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50)
    estudios = models.ManyToManyField(Estudio)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    firma = models.TextField(null=True)
    observacion = models.TextField(null=True)

    def __str__(self):
        return f"{self.id_pedido} - {self.centro} - {self.estado}"

    class Meta:
        db_table = 'pedido'

# estados de la hoja de ruta: pendiente, en_curso, finalizada
class HojaDeRuta(models.Model):
    id_hoja_de_ruta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    transportista = models.ForeignKey(Transportista, on_delete=models.PROTECT)
    pedidos = models.ManyToManyField(Pedido)
    estado = models.CharField(max_length=50)
    hora_comienzo = models.TimeField(null=True)
    hora_fin = models.TimeField(null=True)

    def __str__(self):
        return f"Hoja de ruta #{self.id_hoja_de_ruta} - {self.fecha} - {self.estado}"

    class Meta:
        db_table = 'hoja_de_ruta'