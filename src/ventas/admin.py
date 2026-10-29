from django.contrib import admin

from .models import DetalleVenta, MetodoPago, Venta


admin.site.register(MetodoPago)


class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 0


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    inlines = [DetalleVentaInline]
    list_display = ('id', 'cliente', 'vendedor', 'metodo_pago', 'fecha', 'total', 'activo')
    list_filter = ('metodo_pago', 'vendedor', 'fecha', 'activo')
    search_fields = (
        'cliente__persona__username',
        'cliente__persona__first_name',
        'cliente__persona__last_name',
        'vendedor__persona__username',
    )
    ordering = ('-fecha',)
    date_hierarchy = 'fecha'
    readonly_fields = ('momento_carga',)


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal', 'activo')
    list_filter = ('activo',)
    search_fields = ('producto__nombre',)
    ordering = ('-venta',)
