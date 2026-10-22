from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from .models import Producto, Cpu, Gpu
from .serializers import (
    ProductoSerializer,
    ProductoPublicSerializer,
    CpuSerializer,
    CpuPublicSerializer,
    GpuSerializer,
    Gpu
)

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

    # Autenticacion
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtros, Busqueda y Ordenamiento
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'cant_nucleos': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'cache': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'tdp': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'graficos_integrados': ['exact'],
        'incluye_cooler': ['exact'],
    }
    search_fields = ['socket__nombre', 'arquitectura__nombre']
    ordering_fields = ['cant_nucleos', 'cache', ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CpuPublicSerializer
        else:
            return CpuSerializer


class GpuViewSet(viewsets.ModelViewSet):
    queryset = Gpu.objects.all()
    serializer_class = GpuSerializer
