from django import forms
from .models import Fallecido

class FormFallecido(forms.ModelForm):
    class Meta:
        model = Fallecido
        fields = ['rut', 'nombre', 'apellido_p', 'apellido_m', 'fechafallecimiento', 'ubicacion', 'maps']
        
    # Definición de opciones para el campo ubicación
    UBICACION_CHOICES = [
        ('sotano', 'Sótano'),
        ('bloque_1', 'Bloque 1'),
        ('bloque_2', 'Bloque 2'),
        ('miramar', 'Miramar'),
    ]
    
    ubicacion = forms.ChoiceField(choices=UBICACION_CHOICES, label="Ubicación", required=True)


    
class FallecidoFilterForm(forms.Form):
    # Campos para cada filtro
    rut = forms.CharField(required=False, label="Rut")

    nombre = forms.CharField(required=False, label="Nombre")
    apellido_p = forms.CharField(required=False, label="Apellido Paterno")
    apellido_m = forms.CharField(required=False, label="Apellido Materno")
    
    # Rango de fecha
    fecha_inicio = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha Desde")
    fecha_fin = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha Hasta")
    
    # Ubicación como un desplegable
    ubicacion = forms.ChoiceField(
        choices=[('', 'Seleccione una ubicación')] + Fallecido.UBICACION_CHOICES,
        required=False,
        label="Ubicación"
    )