from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telefono = models.CharField(max_length=30, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.get_full_name() or self.username


class Cliente(models.Model):
    persona = models.OneToOneField(User, on_delete=models.PROTECT, related_name='cliente')
    direccion = models.CharField(max_length=255, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.persona)


class Vendedor(models.Model):
    persona = models.OneToOneField(User, on_delete=models.PROTECT, related_name='vendedor')
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'vendedores'

    def __str__(self):
        return str(self.persona)
