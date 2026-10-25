from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ClienteViewSet, VendedorViewSet

router = DefaultRouter()
router.register(r'personas', UserViewSet, basename='persona')
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'vendedores', VendedorViewSet, basename='vendedor')

urlpatterns = [
    path('', include(router.urls)),
]
