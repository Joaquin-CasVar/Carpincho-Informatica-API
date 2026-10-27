from rest_framework.routers import DefaultRouter

from ventas.views import DetalleVentaViewSet, VentaViewSet
from usuarios.views import UserViewSet, ClienteViewSet, VendedorViewSet

router = DefaultRouter()

#Usuarios
router.register(r'usuarios', UserViewSet, basename='usuario')
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'vendedores', VendedorViewSet, basename='vendedor')

# ventas
router.register(r'ventas', VentaViewSet, basename='ventas-api')
router.register(r'detalles-venta', DetalleVentaViewSet, basename='detalles-venta-api')
