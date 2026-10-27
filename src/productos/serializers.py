from rest_framework import serializers
from .models import (
    Arquitectura,
    Socket,
    Cpu,
    ChipsetGpu,
    Gpu,
    Fabricante,
    Color,
    TipoProducto,
    Producto
)

class ArquitecturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arquitectura
        fields = '__all__'

class SocketSerializer(serializers.ModelSerializer):
    tipo = serializers.StringRelatedField()
    
    class Meta:
        model = Socket
        fields = '__all__'

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = '__all__'

class CpuPublicSerializer(serializers.ModelSerializer):
    arquitectura = ArquitecturaSerializer()
    socket = SocketSerializer()

    class Meta:
        model = Cpu
        fields = [
            "id",
            "cant_nucleos",
            "velocidad_reloj",
            "velocidad_boost",
            "graficos_integrados",
            "cache",
            "incluye_cooler",
            "tdp",
            "arquitectura",
            "socket",
            "producto",
            "activo",
        ]

class ChipsetGpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChipsetGpu
        fields = '__all__'

class GpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gpu
        fields = '__all__'

class GpuPublicSerializer(serializers.ModelSerializer):
    chipset = ChipsetGpuSerializer()
    tipo_memoria = serializers.StringRelatedField()
    refrigeracion = serializers.StringRelatedField()
    
    class Meta:
        model = Gpu
        fields = [
            "id",
            "chipset",
            "tipo_memoria",
            "memoria",
            "velocidad_reloj",
            "velocidad_boost",
            "longitud",
            "ancho_slots",
            "tdp",
            "refrigeracion",
            "producto",
            "activo",
        ]

class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoPublicSerializer(serializers.ModelSerializer):
    detalle_componente = serializers.SerializerMethodField()

    fabricante = FabricanteSerializer()
    color = ColorSerializer()
    tipo = TipoProductoSerializer()

    class Meta:
        model = Producto
        fields = [
                "id",
                "nombre",
                "precio",
                "stock",
                "fabricante",
                "color",
                "tipo",
                "activo",
                'detalle_componente',
            ]

    def get_detalle_componente(self, obj):
        if hasattr(obj, 'cpu'):
            detalle_componente = CpuPublicSerializer(obj.cpu)
        elif hasattr(obj, 'gpu'):
            detalle_componente = GpuPublicSerializer(obj.gpu)
        else:
            return 'No hay detalle'

        return detalle_componente.data
