from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiResponse

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
        if self.request.method == 'GET':
            return VentaListSerializer
        return VentaSerializer

    @extend_schema(
        summary='Borrado lógico de venta',
        description='Desactiva una venta y todos sus detalles sin eliminarlos de la base de datos.',
        responses={
            200: OpenApiResponse(description='Venta desactivada correctamente'),
            403: OpenApiResponse(description='No tiene permisos para realizar esta operación'),
            404: OpenApiResponse(description='Venta no encontrada'),
        }
    )

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

    @extend_schema(
        summary='Borrado lógico de detalle de venta',
        description='Desactiva un detalle de venta sin eliminarlo de la base de datos.',
        responses={
            200: OpenApiResponse(description='Detalle de venta desactivado correctamente'),
            403: OpenApiResponse(description='No tiene permisos para realizar esta operación'),
            404: OpenApiResponse(description='Detalle de venta no encontrado'),
        }
    )

    @action(detail=True, methods=['delete'], permission_classes=[VentaStaffPermission])
    def borrado_logico(self, request, pk=None):
        detalle = self.get_object()
        detalle.activo = False
        detalle.save()
        return Response({'mensaje': f'El detalle {detalle.pk} fue dado de baja'})

    @extend_schema(
        summary='Descontar stock de producto',
        description='Descuenta del stock del producto la cantidad indicada en el detalle de venta. Si el stock es insuficiente, devuelve un error 400.',
        request=None,
        responses={
            200: OpenApiResponse(description='Stock descontado correctamente'),
            400: OpenApiResponse(description='Stock insuficiente'),
            403: OpenApiResponse(description='No tiene permisos para esta operación'),
            404: OpenApiResponse(description='Detalle no encontrado'),
        }
    )

    @action(detail=True, methods=['post'], permission_classes=[VentaStaffPermission])
    def descontar_stock(self, request, pk=None):
        detalle = self.get_object()
        producto = detalle.producto
        if producto.stock < detalle.cantidad:
            return Response({'error': f'Stock insuficiente de {producto.nombre}'}, status=400)
        producto.stock -= detalle.cantidad
        producto.save()
        return Response({'mensaje': 'Stock descontado', 'stock': producto.stock})

    @extend_schema(
            summary='Revertir stock de producto',
            description='Restaura el stock del producto a su valor original antes de la venta.',
            request=None,
            responses={
                200: OpenApiResponse(description='Stock restaurado correctamente'),
                403: OpenApiResponse(description='No tiene permisos para esta operación'),
                404: OpenApiResponse(description='Detalle no encontrado'),
            }
        )

    @action(detail=True, methods=['post'])
    def calcular_subtotal(self, request, pk=None):
        detalle = self.get_object()
        precio = detalle.producto.precio

        # Utiliza el precio del producto para asignarle el precio unitario
        detalle.precio_unitario = precio
        # Calcula el subtotal 
        detalle.subtotal = precio * detalle.cantidad
        detalle.save()

        # Le suma el subtotal al total de la venta
        detalle.venta.total += detalle.subtotal
        detalle.venta.save()

        return Response({
            'mensaje': 'Subtotal y total actualizados',
            'Subtotal del producto': {detalle.subtotal},
            'Total actualizado de la venta': {detalle.venta.total}
        })