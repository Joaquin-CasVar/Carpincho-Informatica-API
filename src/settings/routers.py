from rest_framework.routers import DefaultRouter

from productos.views import CpuViewSet, GpuViewSet, ProductoViewSet

router = DefaultRouter()

# productos
router.register(r'productos', ProductoViewSet, basename='productos-api')
router.register(r'cpus', CpuViewSet, basename='cpus-api')
router.register(r'gpus', GpuViewSet, basename='gpus-api')
