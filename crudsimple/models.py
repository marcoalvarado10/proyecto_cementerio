from django.db import models
from datetime import timedelta

class Fallecido(models.Model):
    UBICACION_CHOICES = [
        ('sotano', 'Sótano'),
        ('bloque_1', 'Bloque 1'),
        ('bloque_2', 'Bloque 2'),
        ('miramar', 'Miramar'),
    ]
    
    PARENTESCO_CHOICES = [
        ('hijo', 'Hijo/a'),
        ('esposo', 'Esposo/a'),
        ('padre', 'Padre/Madre'),
        ('hermano', 'Hermano/a'),
        ('nieto', 'Nieto/a'),
        ('otro', 'Otro'),
    ]
    
    # Datos del fallecido
    rut = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True, verbose_name="Segundo Nombre")  # 👈 AGREGAR ESTA LÍNEA
    apellido_p = models.CharField(max_length=50, blank=True)
    apellido_m = models.CharField(max_length=50, blank=True)
    fechafallecimiento = models.DateField(blank=True, null=True)
    ubicacion = models.CharField(max_length=50, choices=UBICACION_CHOICES, blank=True)
    maps = models.CharField(max_length=500, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")  # 👈 NUEVA LÍNEA

    
    # Datos del familiar responsable
    nombre_familiar = models.CharField(max_length=200, verbose_name="Nombre del Familiar", blank=True, null=True)
    email_familiar = models.EmailField(verbose_name="Email del Familiar", blank=True, null=True)
    telefono_familiar = models.CharField(max_length=15, verbose_name="Teléfono", blank=True, null=True)
    parentesco = models.CharField(max_length=50, verbose_name="Parentesco", choices=PARENTESCO_CHOICES, blank=True, null=True)
    
    # Fechas de mantenimiento (se calculan automáticamente)
    fecha_reduccion = models.DateField(verbose_name="Fecha Reducción (5 años)", blank=True, null=True)
    fecha_mantenimiento_lapida = models.DateField(verbose_name="Mantto. Lápida (2 años)", blank=True, null=True)
    fecha_pintura = models.DateField(verbose_name="Pintura/Retoque (3 años)", blank=True, null=True)
    
    # Control de notificaciones
    notificacion_registro_enviada = models.BooleanField(default=False, verbose_name="Notificación Enviada")
    ultima_notificacion = models.DateField(blank=True, null=True, verbose_name="Última Notificación")
    
    def save(self, *args, **kwargs):
        # Calcular fechas de mantenimiento automáticamente si hay fecha de fallecimiento
        if self.fechafallecimiento:
            if not self.fecha_reduccion:
                self.fecha_reduccion = self.fechafallecimiento + timedelta(days=365*5)
            if not self.fecha_mantenimiento_lapida:
                self.fecha_mantenimiento_lapida = self.fechafallecimiento + timedelta(days=365*2)
            if not self.fecha_pintura:
                self.fecha_pintura = self.fechafallecimiento + timedelta(days=365*3)
        
        super().save(*args, **kwargs)
    
def __str__(self):
    nombre_completo = f"{self.nombre}"
    if self.segundo_nombre:
        nombre_completo += f" {self.segundo_nombre}"
    nombre_completo += f" {self.apellido_p} {self.apellido_m}"
    return nombre_completo