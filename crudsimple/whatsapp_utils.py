from urllib.parse import quote

def generar_link_whatsapp(fallecido):
    """
    Genera un link de WhatsApp con el mensaje de confirmación pre-escrito
    """
    if not fallecido.telefono_familiar:
        return "#"
    
    # Limpiar número de teléfono (solo dígitos)
    telefono = ''.join(filter(str.isdigit, fallecido.telefono_familiar))
    
    # Validar que el teléfono tenga contenido
    if not telefono:
        return "#"
    
    # Asegurar que tenga el código de país de Chile (56)
    # Si el número tiene 9 dígitos y empieza con 9, es un celular chileno
    if len(telefono) == 9 and telefono.startswith('9'):
        telefono = '56' + telefono
    # Si el número tiene 11 dígitos y empieza con 56, está correcto
    elif len(telefono) == 11 and telefono.startswith('56'):
        pass  # Ya está bien formateado
    # Si el número tiene más de 11 dígitos y empieza con +56 o 56
    elif len(telefono) > 11:
        # Buscar el patrón 569XXXXXXXX (Chile)
        if '569' in telefono:
            inicio = telefono.index('569')
            telefono = telefono[inicio:inicio+11]
        else:
            # Intentar extraer los últimos 9 dígitos
            telefono = '56' + telefono[-9:]
    else:
        # Para otros formatos, intentar con el número tal cual
        pass
    
    # Preparar nombres de ubicación
    ubicacion_nombres = {
        'sotano': 'Sótano',
        'bloque_1': 'Bloque 1',
        'bloque_2': 'Bloque 2',
        'miramar': 'Miramar',
    }
    
    # Construir nombre completo
    nombre_completo = fallecido.nombre or ""
    if fallecido.segundo_nombre:
        nombre_completo += f" {fallecido.segundo_nombre}"
    nombre_completo += f" {fallecido.apellido_p or ''} {fallecido.apellido_m or ''}"
    nombre_completo = nombre_completo.strip()
    
    # Crear mensaje
    mensaje = f"""Estimado/a *{fallecido.nombre_familiar}*,

Le confirmamos el registro del fallecido en nuestro sistema:

*DATOS DEL FALLECIDO:*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- *RUT:* {fallecido.rut}
- *Nombre:* {nombre_completo}
- *Fecha:* {fallecido.fechafallecimiento.strftime('%d-%m-%Y') if fallecido.fechafallecimiento else 'N/A'}
- *Ubicación:* {ubicacion_nombres.get(fallecido.ubicacion, fallecido.ubicacion)}
"""
    
    if fallecido.maps:
        mensaje += f"\n📍 *Ver ubicación en Google Maps:*\n{fallecido.maps}\n"
    
    mensaje += f"""
*FECHAS DE MANTENIMIENTO:*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- *Mantenimiento de Lápida:* {fallecido.fecha_mantenimiento_lapida.strftime('%d-%m-%Y') if fallecido.fecha_mantenimiento_lapida else 'N/A'}
- *Pintura/Retoque:* {fallecido.fecha_pintura.strftime('%d-%m-%Y') if fallecido.fecha_pintura else 'N/A'}
- *Reducción (5 años):* {fallecido.fecha_reduccion.strftime('%d-%m-%Y') if fallecido.fecha_reduccion else 'N/A'}

Le enviaremos recordatorios antes de cada fecha.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Si tiene consultas, responda este mensaje.

_Cementerio - Sistema de Administración_"""
    
    # Codificar mensaje para URL
    mensaje_codificado = quote(mensaje)
    
    # Generar link de WhatsApp (sin api, solo wa.me)
    whatsapp_url = f"https://wa.me/{telefono}?text={mensaje_codificado}"
    
    print(f"DEBUG - Teléfono formateado: {telefono}")  # Para debug
    print(f"DEBUG - URL generada: {whatsapp_url[:100]}...")  # Para debug
    
    return whatsapp_url


def generar_mensaje_mantenimiento(fallecido, tipo_mantenimiento):
    """
    Genera mensaje de recordatorio de mantenimiento
    tipo_mantenimiento: 'lapida', 'pintura', 'reduccion'
    """
    if not fallecido.telefono_familiar:
        return "#"
    
    # Limpiar y formatear teléfono
    telefono = ''.join(filter(str.isdigit, fallecido.telefono_familiar))
    
    if not telefono:
        return "#"
    
    if len(telefono) == 9 and telefono.startswith('9'):
        telefono = '56' + telefono
    elif len(telefono) == 11 and telefono.startswith('56'):
        pass
    
    mensajes = {
        'lapida': f"""Estimado/a *{fallecido.nombre_familiar}*,

⏰ *RECORDATORIO DE MANTENIMIENTO*

Le recordamos que se aproxima la fecha de *mantenimiento de lápida* para:

- *{fallecido.nombre} {fallecido.apellido_p} {fallecido.apellido_m}*
- *Fecha programada:* {fallecido.fecha_mantenimiento_lapida.strftime('%d-%m-%Y') if fallecido.fecha_mantenimiento_lapida else 'N/A'}
- *Ubicación:* {fallecido.ubicacion}

Por favor, coordine la visita con anticipación.

_Cementerio - Sistema de Administración_""",
        
        'pintura': f"""Estimado/a *{fallecido.nombre_familiar}*,

⏰ *RECORDATORIO DE MANTENIMIENTO*

Le recordamos que se aproxima la fecha de *pintura/retoque* para:

- *{fallecido.nombre} {fallecido.apellido_p} {fallecido.apellido_m}*
- *Fecha programada:* {fallecido.fecha_pintura.strftime('%d-%m-%Y') if fallecido.fecha_pintura else 'N/A'}
- *Ubicación:* {fallecido.ubicacion}

Recomendamos realizar el mantenimiento a tiempo.

_Cementerio - Sistema de Administración_""",
        
        'reduccion': f"""Estimado/a *{fallecido.nombre_familiar}*,

⚠️ *RECORDATORIO IMPORTANTE - REDUCCIÓN*

Le recordamos que se aproxima la fecha de *reducción* (5 años) para:

- *{fallecido.nombre} {fallecido.apellido_p} {fallecido.apellido_m}*
- *Fecha programada:* {fallecido.fecha_reduccion.strftime('%d-%m-%Y') if fallecido.fecha_reduccion else 'N/A'}
- *Ubicación:* {fallecido.ubicacion}

Este es un proceso obligatorio. Por favor, contacte a la administración con anticipación.

_Cementerio - Sistema de Administración_"""
    }
    
    mensaje = mensajes.get(tipo_mantenimiento, "")
    mensaje_codificado = quote(mensaje)
    whatsapp_url = f"https://wa.me/{telefono}?text={mensaje_codificado}"
    
    return whatsapp_url