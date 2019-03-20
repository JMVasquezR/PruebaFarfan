from rest_framework import serializers

from app_nucleo.models import Clientes, Producto, ProductCliente, TipoDocumento


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'


class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoClienteSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(many=True)
    producto = ProductoSerializer(many=True)

    class Meta:
        model = ProductCliente
        fields = ('cliente', 'producto')
