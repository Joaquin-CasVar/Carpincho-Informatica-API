from rest_framework import serializers
from .models import Cpu, Gpu, Producto

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = '__all__'

class GpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gpu
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoPublicSerializer(serializers.ModelSerializer):
    detalle_componente = serializers.SerializerMethodField()

    fabricante = serializers.StringRelatedField()
    color = serializers.StringRelatedField()
    tipo = serializers.StringRelatedField()

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
        if (obj.tipo.id) == 1 and hasattr(obj, 'cpu'):
            detalle_componente = CpuSerializer(obj.cpu)
        elif (obj.tipo.id) == 2 and hasattr(obj, 'gpu'):
            detalle_componente = GpuSerializer(obj.gpu)
        else:
            return 'No hay detalle'

        return detalle_componente.data

