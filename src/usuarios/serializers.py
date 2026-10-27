from rest_framework import serializers
from .models import User, Cliente, Vendedor

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [ # noqa: RUF012
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'telefono', 
            'activo',
        ]   
        read_only_fields = ['id']  # noqa: RUF012

class ClienteSerializer(serializers.ModelSerializer):
    persona = UserSerializer(read_only=True)

    persona_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source="persona",
        write_only=True
    )

    class Meta:
        model = Cliente
        fields = [ # noqa: RUF012
            'id', 
            'persona', 
            'persona_id',
            'direccion', 
            'activo',
        ]
        read_only_fields = ['persona']  # noqa: RUF012

class VendedorSerializer(serializers.ModelSerializer):
    persona = UserSerializer(read_only=True)

    persona_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source="persona",
        write_only=True
    )

    class Meta:
        model = Vendedor
        fields = [ # noqa: RUF012
            'id', 
            'persona', 
            'persona_id',
            'salario', 
            'activo',
        ]
        read_only_fields = ['id']  # noqa: RUF012