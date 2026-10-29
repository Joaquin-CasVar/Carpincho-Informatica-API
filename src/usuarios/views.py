from .models import User, Cliente, Vendedor
from .serializers import UserSerializer, ClienteSerializer, VendedorSerializer
from django_filters.rest_framework import DjangoFilterBackend

from drf_spectacular.openapi import AutoSchema

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

# Create your views here.

#Paginado local
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Mixin compartido para el borrado logico del modelo User, Cliente y Vendedor
class BorradoLogicoMixin:

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.activo = False
        instance.save()

        return Response(
            {"detail": "Registro desactivado correctamente"},
            status=status.HTTP_200_OK
        )

#ViewSets para los modelo Persona (User) 
class UserViewSet(BorradoLogicoMixin, viewsets.ModelViewSet):
    queryset = User.objects.filter(activo=True)  # Solo trae usuarios activos
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] # noqa: RUF012
    model_name = "Usuario"
    
    # Filtros y búsquedas para Persona
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] # noqa: RUF012
    filterset_fields = ['username'] # noqa: RUF012
    search_fields = ['username', 'telefono'] # noqa: RUF012
    ordering_fields = ['id', 'username'] # noqa: RUF012


#ViewSets para el modelo Cliente
class ClienteViewSet(BorradoLogicoMixin, viewsets.ModelViewSet):
    queryset = Cliente.objects.filter(activo=True).select_related('persona')
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated] # noqa: RUF012
    pagination_class = StandardResultsSetPagination
    model_name = "Cliente"
    
    # Filtros y Búsqueda
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] # noqa: RUF012
    filterset_fields = ['direccion', 'persona__email'] # noqa: RUF012
    search_fields = ['direccion', 'persona__username', 'persona__first_name', 'persona__last_name'] # noqa: RUF012
    ordering_fields = ['id', 'persona__username'] # noqa: RUF012


#ViewSets para el modelo Vendedor
class VendedorViewSet(BorradoLogicoMixin, viewsets.ModelViewSet):
    queryset = Vendedor.objects.filter(activo=True).select_related('persona')
    serializer_class = VendedorSerializer
    permission_classes = [IsAuthenticated] # noqa: RUF012
    pagination_class = StandardResultsSetPagination
    model_name = "Vendedor"
    
    # Filtros y Búsqueda
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] # noqa: RUF012
    filterset_fields = ['salario'] # noqa: RUF012
    search_fields = ['persona__username', 'persona__first_name', 'persona__last_name', 'persona__telefono'] # noqa: RUF012
    ordering_fields = ['id', 'salario', 'persona__username'] # noqa: RUF012
