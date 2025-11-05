from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def enviar_notificacion_registro(fallecido):
    """
    Envía email de confirmación al familiar cuando se registra un fallecido
    """
    if not fallecido.email_familiar:
        return False
    
    # Asunto del correo
    asunto = f'Confirmación de Registro - {fallecido.nombre} {fallecido.apellido_p}'
    
    # Preparar datos para el email
    ubicacion_nombres = {
        'sotano': 'Sótano',
        'bloque_1': 'Bloque 1',
        'bloque_2': 'Bloque 2',
        'miramar': 'Miramar',
    }
    
    # Crear el cuerpo del mensaje
    mensaje = f"""
Estimado/a {fallecido.nombre_familiar},

Le confirmamos el registro del fallecido en nuestro sistema:

DATOS DEL FALLECIDO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- RUT: {fallecido.rut}
- Nombre: {fallecido.nombre} {fallecido.apellido_p} {fallecido.apellido_m}
- Fecha de Fallecimiento: {fallecido.fechafallecimiento.strftime('%d-%m-%Y') if fallecido.fechafallecimiento else 'N/A'}
- Ubicación: {ubicacion_nombres.get(fallecido.ubicacion, fallecido.ubicacion)}

UBICACIÓN EN GOOGLE MAPS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    if fallecido.maps:
        mensaje += f"📍 Ver ubicación exacta: {fallecido.maps}\n\n"
    else:
        mensaje += "No se registró ubicación en Google Maps.\n\n"
    
    mensaje += f"""
FECHAS DE MANTENIMIENTO PROGRAMADAS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Mantenimiento de Lápida: {fallecido.fecha_mantenimiento_lapida.strftime('%d-%m-%Y') if fallecido.fecha_mantenimiento_lapida else 'N/A'}
- Pintura/Retoque: {fallecido.fecha_pintura.strftime('%d-%m-%Y') if fallecido.fecha_pintura else 'N/A'}
- Reducción (5 años): {fallecido.fecha_reduccion.strftime('%d-%m-%Y') if fallecido.fecha_reduccion else 'N/A'}

Le enviaremos recordatorios antes de cada fecha de mantenimiento.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Si tiene alguna consulta, no dude en contactarnos.

Atentamente,
Sistema de Administración del Cementerio
"""
    
    try:
        send_mail(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [fallecido.email_familiar],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error al enviar email: {e}")
        return False