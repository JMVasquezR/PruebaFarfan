from django.db import models
import datetime

GENERO = (
    ('m', 'Masculino'),
    ('f', 'Femenino'),
)

TYPE_PATTERN = (
    (0, 'Numerico'),
    (1, 'Alfanumerico'),
)

TYPE_TAXPAYER = (
    (0, 'Documento para nacionales solamente'),
    (1, 'Documento para extranjeros solamente'),
    (2, 'Documento para nacionales y extranjeros'),
)

TYPE_LENGTH = (
    (0, 'Exacta'),
    (1, 'Inexacta'),
)


class TipoDocumento(models.Model):
    name_short = models.CharField(blank=False, null=False, max_length=25)
    name_long = models.CharField(blank=False, null=False, max_length=100)
    type_pattern = models.IntegerField(blank=False, null=False, choices=TYPE_PATTERN)
    type_taxpayer = models.IntegerField(blank=False, null=False, choices=TYPE_TAXPAYER)
    type_length = models.IntegerField(blank=False, null=False, choices=TYPE_LENGTH)
    length = models.IntegerField(blank=False, null=False, default=0)


class Clientes(models.Model):
    nombre_completo = models.CharField(blank=False, null=False, max_length=150)
    apellido_paterno = models.CharField(blank=False, null=False, max_length=100)
    apellido_materno = models.CharField(blank=False, null=False, max_length=100)
    direccion = models.CharField(blank=False, null=False, max_length=100)
    genero = models.CharField(blank=False, null=False, choices=GENERO, max_length=1)
    numero_documento = models.CharField(blank=False, null=False, max_length=12)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=False)


class Producto(models.Model):
    nombre = models.CharField(blank=False, null=False, max_length=100)
    descripcion = models.CharField(blank=False, null=False, max_length=200)
    fecha_creacion = models.DateTimeField(auto_now=datetime.datetime.now())
    cliente = models.ManyToManyField(Clientes, blank=True, related_name='products', through="ProductCliente")


class ProductCliente(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
