from django.db import models


class Fabricante(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Color(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class TipoProducto(models.Model):
    tipo = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'tipo de producto'
        verbose_name_plural = 'tipos de producto'

    def __str__(self):
        return self.tipo


class Producto(models.Model):
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT, related_name='productos')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='productos')
    tipo = models.ForeignKey(TipoProducto, on_delete=models.PROTECT, related_name='productos')
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.CharField(max_length=256, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Arquitectura(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class TipoSocket(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'tipo de socket'
        verbose_name_plural = 'tipos de socket'

    def __str__(self):
        return self.nombre


class Socket(models.Model):
    tipo = models.ForeignKey(TipoSocket, on_delete=models.PROTECT, related_name='sockets')
    nombre = models.CharField(max_length=100)
    n_pines = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


class TipoMemoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'tipo de memoria'
        verbose_name_plural = 'tipos de memoria'

    def __str__(self):
        return self.nombre


class ChipsetGpu(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'chipset GPU'
        verbose_name_plural = 'chipsets GPU'

    def __str__(self):
        return self.nombre


class Refrigeracion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'refrigeración'
        verbose_name_plural = 'refrigeraciones'

    def __str__(self):
        return self.nombre


class Cpu(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='cpu')
    arquitectura = models.ForeignKey(Arquitectura, on_delete=models.PROTECT, related_name='cpu')
    socket = models.ForeignKey(Socket, on_delete=models.PROTECT, related_name='cpu')
    cant_nucleos = models.PositiveIntegerField()
    velocidad_reloj = models.DecimalField(max_digits=5, decimal_places=2)
    velocidad_boost = models.DecimalField(max_digits=5, decimal_places=2)
    graficos_integrados = models.BooleanField(default=False)
    cache = models.PositiveIntegerField()
    incluye_cooler = models.BooleanField(default=False)
    tdp = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'CPU'
        verbose_name_plural = 'CPUs'

    def __str__(self):
        return str(self.producto)


class Gpu(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='gpu')
    tipo_memoria = models.ForeignKey(TipoMemoria, on_delete=models.PROTECT, related_name='gpu')
    chipset = models.ForeignKey(ChipsetGpu, on_delete=models.PROTECT, related_name='gpu')
    refrigeracion = models.ForeignKey(Refrigeracion, on_delete=models.PROTECT, related_name='gpu')
    memoria = models.PositiveIntegerField()
    velocidad_reloj = models.PositiveIntegerField()
    velocidad_boost = models.PositiveIntegerField()
    longitud = models.PositiveIntegerField()
    ancho_slots = models.DecimalField(max_digits=3, decimal_places=1)
    tdp = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPUs'

    def __str__(self):
        return str(self.producto)
