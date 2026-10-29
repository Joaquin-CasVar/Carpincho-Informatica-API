from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import (
    Producto,
    Cpu,
    Gpu,
    Fabricante,
    Color,
    TipoProducto,
    Arquitectura,
    Socket,
    ChipsetGpu,
)

from .permissions import ProductoStaffOrReadOnlyPermission

from .serializers import (
    ProductoSerializer,
    ProductoPublicSerializer,
    FabricanteSerializer,
    ColorSerializer,
    TipoProductoSerializer,
    CpuSerializer,
    CpuPublicSerializer,
    ArquitecturaSerializer,
    SocketSerializer,
    GpuSerializer,
    GpuPublicSerializer,
    ChipsetGpuSerializer,
)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()

    # Autenticacion
    permission_classes = [ProductoStaffOrReadOnlyPermission]

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

        if hasattr(producto, 'cpu'):
            producto.cpu.activo = False
            producto.cpu.save()
        elif hasattr(producto, 'gpu'):
            producto.gpu.activo = False
            producto.gpu.save()

        producto.save()
        return Response({'status': 'Producto y componente relacionado desactivados'})

class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all()

    # Autenticacion
    permission_classes = [ProductoStaffOrReadOnlyPermission]

    # Filtros, Busqueda y Ordenamiento
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'arquitectura': ['exact'],
        'socket': ['exact'],
        'cant_nucleos': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'cache': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'tdp': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'graficos_integrados': ['exact'],
        'incluye_cooler': ['exact'],
    }
    search_fields = ['socket__nombre', 'arquitectura__nombre']
    ordering_fields = ['cant_nucleos', 'cache']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CpuPublicSerializer
        else:
            return CpuSerializer


class GpuViewSet(viewsets.ModelViewSet):
    queryset = Gpu.objects.all()

    # Autenticacion
    permission_classes = [ProductoStaffOrReadOnlyPermission]

    # Filtros, Busqueda y Ordenamiento
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'chipset': ['exact'],
        'memoria': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'refrigeracion': ['exact']
    }
    search_fields = ['chipset__nombre', 'refrigeracion__nombre']
    ordering_fields = ['memoria', 'chipset__nombre', 'velocidad_boost']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GpuPublicSerializer
        else:
            return GpuSerializer


class FabricanteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
    permission_classes = [AllowAny]

class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [AllowAny]

class TipoProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer
    permission_classes = [AllowAny]

class ArquitecturaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Arquitectura.objects.all()
    serializer_class = ArquitecturaSerializer
    permission_classes = [AllowAny]

class SocketViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Socket.objects.all()
    serializer_class = SocketSerializer
    permission_classes = [AllowAny]

class ChipsetGpuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChipsetGpu.objects.all()
    serializer_class = ChipsetGpuSerializer
    permission_classes = [AllowAny]
