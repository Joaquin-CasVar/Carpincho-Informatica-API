from rest_framework import serializers
from .models import User, Cliente, Vendedor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [  # noqa: RUF012
            'id',
            'username',  # Requerido por AbstractUser para crear el usuario
            'password',  # Requerido para poder asignarle una clave al crear
            'telefono',
            'activo'
        ]
        read_only_fields = ['id']  # noqa: RUF012
        extra_kwargs = { # noqa: RUF012
            'password': {'write_only': True, 'required': False},
            'activo': {'read_only': True}  # Se maneja por el borrado lógico en la vista
        }


class ClienteSerializer(serializers.ModelSerializer):
    persona = UserSerializer()  # Hacemos que sea un nested serializer obligatorio

    class Meta:
        model = Cliente
        fields = [  # noqa: RUF012
            'id',
            'persona',
            'direccion',
            'activo'
        ]
        read_only_fields = ['id']  # noqa: RUF012
        extra_kwargs = { # noqa: RUF012
            'activo': {'read_only': True}
        }

    def create(self, validated_data):
        # Separamos los datos de la persona de los del cliente
        persona_data = validated_data.pop('persona')
        password = persona_data.pop('password', None)
        
        # Creamos primero el usuario usando el modelo
        persona = User.objects.create(**persona_data)
        if password:
            persona.set_password(password)
            persona.save()
            
        # Creamos el cliente asociándolo a la persona que acabamos de crear
        cliente = Cliente.objects.create(persona=persona, **validated_data)
        return cliente

    def update(self, instance, validated_data):
        # Separamos los datos anidados de la persona si vienen en la petición
        persona_data = validated_data.pop('persona', None)
        
        if persona_data:
            persona_instance = instance.persona
            password = persona_data.pop('password', None)
            
            # Actualizamos los campos de la persona uno a uno
            for attr, value in persona_data.items():
                setattr(persona_instance, attr, value)
            
            if password:
                persona_instance.set_password(password)
                
            persona_instance.save()
            
        # Actualizamos los campos propios del cliente (ej: direccion)
        return super().update(instance, validated_data)


class VendedorSerializer(serializers.ModelSerializer):
    persona = UserSerializer()  # Hacemos que sea un nested serializer obligatorio

    class Meta:
        model = Vendedor
        fields = [  # noqa: RUF012
            'id',
            'persona',
            'salario',
            'activo'
        ]
        read_only_fields = ['id']  # noqa: RUF012
        extra_kwargs = { # noqa: RUF012
            'activo': {'read_only': True}
        }

    def create(self, validated_data):
        persona_data = validated_data.pop('persona')
        password = persona_data.pop('password', None)
        
        persona = User.objects.create(**persona_data)
        if password:
            persona.set_password(password)
            persona.save()
            
        vendedor = Vendedor.objects.create(persona=persona, **validated_data)
        return vendedor

    def update(self, instance, validated_data):
        persona_data = validated_data.pop('persona', None)
        
        if persona_data:
            persona_instance = instance.persona
            password = persona_data.pop('password', None)
            
            for attr, value in persona_data.items():
                setattr(persona_instance, attr, value)
                
            if password:
                persona_instance.set_password(password)
                
            persona_instance.save()
            
        return super().update(instance, validated_data)
