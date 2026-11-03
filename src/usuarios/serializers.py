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

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields =[
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'telefono',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            telefono=validated_data['telefono'],
            password=validated_data['password'],
        )
        return user


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