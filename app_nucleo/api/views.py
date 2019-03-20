from rest_framework import viewsets

from app_nucleo.api.serializers import ClienteSerializer, ProductoSerializer, TipoDocumentoSerializer, \
    ProductoClienteSerializer
from app_nucleo.models import Clientes, Producto, ProductCliente, TipoDocumento


class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Clientes.objects.all()


class TipoDocumentoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoDocumentoSerializer
    queryset = TipoDocumento.objects.all()


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()


class ProductoClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoClienteSerializer
    queryset = ProductCliente.objects.all()
