from django.db import models

class Fallecido(models.Model):
    UBICACION_CHOICES = [
        ('sotano', 'Sótano'),
        ('bloque_1', 'Bloque 1'),
        ('bloque_2', 'Bloque 2'),
        ('miramar', 'Miramar'),
    ]

    rut = models.CharField(max_length=50, blank=True)  # Permite que este campo esté en blanco
    nombre = models.CharField(max_length=50, blank=True)  # Permite que este campo esté en blanco
    apellido_p = models.CharField(max_length=50, blank=True)  # Permite que este campo esté en blanco
    apellido_m = models.CharField(max_length=50, blank=True)  # Permite que este campo esté en blanco
    fechafallecimiento = models.DateField(blank=True, null=True)  # Permite que este campo esté en blanco
    ubicacion = models.CharField(max_length=50, choices=UBICACION_CHOICES, blank=True)  # Con opciones predeterminadas
    maps = models.CharField(max_length=50, blank=True)  # Permite que este campo esté en blanco

    def __str__(self):
        return self.nombre
