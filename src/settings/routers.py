from rest_framework.routers import DefaultRouter

from usuarios.views import UserViewSet, ClienteViewSet, VendedorViewSet

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuario')
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'vendedores', VendedorViewSet, basename='vendedor')