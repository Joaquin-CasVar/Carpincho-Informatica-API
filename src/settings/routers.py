from rest_framework.routers import DefaultRouter

from ventas.views import DetalleVentaViewSet, VentaViewSet

router = DefaultRouter()

# ventas
router.register(r'ventas', VentaViewSet, basename='ventas-api')
router.register(r'detalles-venta', DetalleVentaViewSet, basename='detalles-venta-api')
