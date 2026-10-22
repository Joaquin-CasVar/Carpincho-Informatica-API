from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from .models import Producto, Cpu, Gpu
from .serializers import ProductoSerializer, ProductoPublicSerializer, CpuSerializer, GpuSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()

    # Autenticacion
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtros, Busqueda y Ordenamiento
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'fabricante': ['exact'],
        'color': ['exact'],
        'tipo': ['exact'],
        'precio': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'stock': ['exact', 'gt', 'lt', 'gte', 'lte'],
    }
    search_fields = ['nombre', 'fabricante__nombre']
    ordering_fields = ['nombre', 'precio', 'tipo']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductoPublicSerializer
        else:
            return ProductoSerializer

    # Funcion personalizada borrado logico del producto y su componente relacionado
    @action(detail=True, methods=['delete'])
    def borrado_logico(self, request, pk=None):
        producto = self.get_object()
        producto.activo = False

        if (producto.tipo.id) == 1 and hasattr(producto, 'cpu'):
            producto.cpu.activo = False
            producto.cpu.save()
        elif (producto.tipo.id) == 2 and hasattr(producto, 'gpu'):
            producto.gpu.activo = False
            producto.gpu.save()

        producto.save()
        return Response({'status': 'Producto y componente relacionado desactivados'})

class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

class GpuViewSet(viewsets.ModelViewSet):
    queryset = Gpu.objects.all()
    serializer_class = GpuSerializer
