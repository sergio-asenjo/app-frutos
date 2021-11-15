from django.db import models

# Create your models here.

ESTADOS_ENVIOS = (
    ('Por Enviar', 'por enviar'),
    ('Entregado', 'entregado'),
)

class Despacho(models.Model):
    # Datos del Cliente.
    nombre_cliente = models.CharField(max_length=100)
    dirección_cliente = models.CharField(max_length=150)
    telefono_cliente = models.CharField(max_length=20)
    # Datos del Envío.
    numero_despacho = models.CharField(max_length=30, unique=True)
    productos_cliente = models.TextField()
    peso_productos = models.PositiveIntegerField()
    fecha_ingreso_despacho = models.DateField()
    fecha_envio_despacho = models.DateField()
    estado_despacho = models.CharField(max_length=50, choices=ESTADOS_ENVIOS, default='Por Enviar')
    # Medidas del Paquete.
    profundidad_despacho = models.PositiveIntegerField()
    ancho_despacho = models.PositiveIntegerField()
    alto_despacho = models.PositiveIntegerField()