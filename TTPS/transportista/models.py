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

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50)
    estudios = models.ManyToManyField(Estudio)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    hoja_de_ruta_id = models.ForeignKey('HojaDeRuta', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id_pedido} - {self.centro} - {self.estado}"

    class Meta:
        db_table = 'pedido'


class HojaDeRuta(models.Model):
    id_hoja_de_ruta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    transportista = models.ForeignKey(Transportista, on_delete=models.PROTECT)
    pedidos = models.ManyToManyField(Pedido)
    estado = models.CharField(max_length=50)
    hora_comienzo = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f""

    class Meta:
        db_table = 'hoja_de_ruta'