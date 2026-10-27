from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import DetalleVenta, Venta
from .permissions import VentaStaffPermission
from .serializers import DetalleVentaSerializer, VentaListSerializer, VentaSerializer


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.filter(activo=True).select_related(
        'cliente', 'vendedor', 'metodo_pago'
    ).prefetch_related('detalles').order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'cliente': ['exact'],
        'vendedor': ['exact'],
        'metodo_pago': ['exact'],
        'fecha': ['exact', 'gte', 'lte'],
        'total': ['gte', 'lte'],
    }
    search_fields = [
        'cliente__persona__username',
        'cliente__persona__first_name',
        'cliente__persona__last_name',
        'vendedor__persona__username',
    ]
    ordering_fields = ['fecha', 'total', 'id']

    def get_serializer_class(self):
        if self.action == 'list':
            return VentaListSerializer
        return VentaSerializer

    @action(detail=True, methods=['delete'], permission_classes=[VentaStaffPermission])
    def borrado_logico(self, request, pk=None):
        venta = self.get_object()
        venta.activo = False
        venta.save()
        venta.detalles.update(activo=False)
        return Response({'mensaje': f'La venta {venta.pk} fue dada de baja'})


class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.filter(activo=True).select_related('producto').order_by('id')
    serializer_class = DetalleVentaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['venta']

    @action(detail=True, methods=['delete'], permission_classes=[VentaStaffPermission])
    def borrado_logico(self, request, pk=None):
        detalle = self.get_object()
        detalle.activo = False
        detalle.save()
        return Response({'mensaje': f'El detalle {detalle.pk} fue dado de baja'})

    @action(detail=True, methods=['post'], permission_classes=[VentaStaffPermission])
    def descontar_stock(self, request, pk=None):
        detalle = self.get_object()
        producto = detalle.producto
        if producto.stock < detalle.cantidad:
            return Response({'error': f'Stock insuficiente de {producto.nombre}'}, status=400)
        producto.stock -= detalle.cantidad
        producto.save()
        return Response({'mensaje': 'Stock descontado', 'stock': producto.stock})
