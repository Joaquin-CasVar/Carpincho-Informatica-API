from django.contrib import admin

from .models import (
    Fabricante,
    Color,
    TipoProducto,
    Producto,
    Arquitectura,
    TipoSocket,
    Socket,
    Cpu,
    TipoMemoria,
    ChipsetGpu,
    Refrigeracion,
    Gpu
)


admin.site.register(Fabricante)
admin.site.register(Color)
admin.site.register(TipoProducto)
admin.site.register(Arquitectura)
admin.site.register(TipoSocket)
admin.site.register(Socket)
admin.site.register(TipoMemoria)
admin.site.register(ChipsetGpu)
admin.site.register(Refrigeracion)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fabricante', 'tipo', 'color', 'precio', 'stock', 'activo')
    list_filter = ('fabricante', 'tipo', 'color', 'activo')
    search_fields = ('nombre', 'fabricante__nombre')
    ordering = ('nombre',)


@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
    list_display = ('producto', 'arquitectura', 'socket', 'cant_nucleos', 'tdp', 'activo')
    list_filter = ('arquitectura', 'socket', 'graficos_integrados', 'incluye_cooler', 'activo')
    search_fields = ('producto__nombre', 'arquitectura__nombre', 'socket__nombre')
    ordering = ('producto__nombre',)


@admin.register(Gpu)
class GpuAdmin(admin.ModelAdmin):
    list_display = ('producto', 'chipset', 'tipo_memoria', 'memoria', 'tdp', 'activo')
    list_filter = ('chipset', 'tipo_memoria', 'refrigeracion', 'activo')
    search_fields = ('producto__nombre', 'chipset__nombre')
    ordering = ('producto__nombre',)
