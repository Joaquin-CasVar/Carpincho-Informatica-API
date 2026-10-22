from django.contrib import admin

from .models import (
    Fabricante,
    Color,
    TipoProducto,
    Arquitectura,
    TipoSocket,
    Socket,
    TipoMemoria,
    ChipsetGpu,
    Refrigeracion
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
