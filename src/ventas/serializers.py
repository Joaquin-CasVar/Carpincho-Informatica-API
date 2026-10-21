from rest_framework import serializers

from .models import DetalleVenta, Venta


class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ['id', 'venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal']
        read_only_fields = ['id']


class VentaListSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True, read_only=True)

    class Meta:
        model = Venta
        fields = [
            'id', 'cliente', 'vendedor', 'metodo_pago', 'fecha',
            'total', 'momento_carga', 'detalles',
        ]


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = [
            'id', 'cliente', 'vendedor', 'metodo_pago', 'fecha',
            'total', 'momento_carga',
        ]
        read_only_fields = ['id', 'momento_carga']
