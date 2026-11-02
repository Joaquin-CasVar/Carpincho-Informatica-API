from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Cliente, User, Vendedor


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Datos extra', {'fields': ('telefono', 'activo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Datos extra', {'fields': ('telefono', 'activo')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'telefono', 'is_staff', 'activo')
    list_filter = ('is_staff', 'is_active', 'activo')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('persona', 'direccion', 'activo')
    list_filter = ('activo',)
    search_fields = ('persona__username', 'persona__first_name', 'persona__last_name', 'direccion')
    ordering = ('persona__username',)


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('persona', 'salario', 'activo')
    list_filter = ('activo',)
    search_fields = ('persona__username', 'persona__first_name', 'persona__last_name')
    ordering = ('persona__username',)
