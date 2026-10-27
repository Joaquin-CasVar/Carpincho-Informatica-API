from rest_framework.routers import DefaultRouter

from productos.views import (
    CpuViewSet,
    GpuViewSet,
    ProductoViewSet,
    FabricanteViewSet,
    ColorViewSet,
    TipoProductoViewSet,
    ArquitecturaViewSet,
    SocketViewSet,
    ChipsetGpuViewSet
)

router = DefaultRouter()

# productos
router.register(r'productos', ProductoViewSet, basename='productos-api')
router.register(r'cpus', CpuViewSet, basename='cpus-api')
router.register(r'gpus', GpuViewSet, basename='gpus-api')
router.register(r'fabricantes', FabricanteViewSet, basename='fabricantes-api')
router.register(r'colores', ColorViewSet, basename='colores-api')
router.register(r'tipos-producto', TipoProductoViewSet, basename='tipos-producto-api')
router.register(r'arquitecturas', ArquitecturaViewSet, basename='arquitecturas-api')
router.register(r'sockets', SocketViewSet, basename='sockets-api')
router.register(r'chipsets-gpu', ChipsetGpuViewSet, basename='chipsets-gpu-api')
