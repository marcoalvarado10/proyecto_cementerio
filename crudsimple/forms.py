from django import forms
from .models import Fallecido

class FormFallecido(forms.ModelForm):
    class Meta:
        model = Fallecido
        fields = [
            'rut', 'nombre', 'segundo_nombre', 'apellido_p', 'apellido_m',
            'fechafallecimiento', 'ubicacion', 'maps',
            'latitud', 'longitud', 'foto', 'historia',
            'nombre_familiar', 'email_familiar', 'telefono_familiar', 'parentesco'
        ]
        widgets = {
            'maps': forms.TextInput(attrs={'placeholder': 'https://maps.google.com/...'}),
            'email_familiar': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
            'telefono_familiar': forms.TextInput(attrs={'placeholder': '+56 9 1234 5678'}),
            'historia': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Historia del fallecido...'}),
        }

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