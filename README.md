# 🏛️ Sistema de Administración de Cementerio - QEPD

Sistema web completo desarrollado en Django para la gestión integral de cementerios con georreferenciación GPS, notificaciones automáticas y gestión de historias de fallecidos.

## ✨ Características Principales

### 📋 Gestión de Fallecidos
- ✅ Registro completo con validación de RUT chileno automática
- ✅ Campo de segundo nombre
- ✅ Fotos de fallecidos con visualización
- ✅ Historia/reseña personalizada de cada fallecido
- ✅ Página de detalles completos por fallecido
- ✅ Gestión de información de familiares responsables
- ✅ Restricción de fechas (no permite fechas futuras)

### 🗺️ Georreferenciación GPS
- ✅ Mapa embebido con Google Maps API
- ✅ Vista satelital de ubicación exacta de tumbas
- ✅ Coordenadas GPS (latitud/longitud)
- ✅ Botón "Cómo Llegar" con navegación GPS
- ✅ Integración completa con Google Maps

### 📱 Notificaciones Automáticas
- ✅ WhatsApp automático al agregar fallecido
- ✅ Mensaje personalizado con datos completos
- ✅ Link de Google Maps incluido
- ✅ Fechas de mantenimiento en el mensaje

### 📅 Sistema de Mantenimiento
- ✅ Cálculo automático de fechas:
  - Mantenimiento de lápida: 2 años
  - Pintura/retoque: 3 años  
  - Reducción: 5 años

### 📊 Dashboard y Reportes
- ✅ Estadísticas en tiempo real
- ✅ Total de fallecidos
- ✅ Registrados hoy
- ✅ Ubicación con más fallecidos
- ✅ Registros última semana
- ✅ Exportación a Excel por categoría

### 🔍 Búsqueda Avanzada
- ✅ Búsqueda desde página principal
- ✅ Filtros por: RUT, nombre, apellidos, fecha, ubicación
- ✅ Búsqueda combinada
- ✅ Resultados en tiempo real

### 🎨 Interfaz de Usuario
- ✅ Diseño responsive con Bootstrap 5
- ✅ Formulario colapsable organizado por secciones
- ✅ Iconos Font Awesome
- ✅ Mensajes de éxito/error con auto-ocultado
- ✅ Modal de edición completo

## 🚀 Instalación

### Requisitos Previos
- Python 3.13 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Clonar o Descargar

Descarga el proyecto en tu computadora.

### Paso 2: Instalar Dependencias
```bash
pip install django pymysql openpyxl cryptography Pillow
```

### Paso 3: Configurar Google Maps API

1. Obtén una API Key de Google Maps:
   - Ve a: https://console.cloud.google.com/
   - Habilita: Maps JavaScript API y Geocoding API
   - Crea una API Key

2. Abre `eva2/settings.py` y agrega al final:
```python
GOOGLE_MAPS_API_KEY = 'TU_API_KEY_AQUI'
```

### Paso 4: Configurar Base de Datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### Paso 5: Crear Usuario Administrador
```bash
python manage.py createsuperuser
```

Ingresa:
- Username: (tu usuario)
- Email: (presiona Enter para omitir)
- Password: (tu contraseña)

### Paso 6: Ejecutar el Servidor
```bash
python manage.py runserver
```

El sistema estará disponible en: **http://127.0.0.1:8000/**

## 🔐 Acceso al Sistema

### URLs Principales
- **Página Principal:** http://127.0.0.1:8000/
- **Iniciar Sesión:** http://127.0.0.1:8000/login/
- **Dashboard:** http://127.0.0.1:8000/dashboard/
- **Lista Fallecidos:** http://127.0.0.1:8000/fallecidos/

### Credenciales
Usa el usuario y contraseña que creaste con `createsuperuser`.

## 📖 Uso del Sistema

### 1. Agregar un Fallecido

1. Inicia sesión
2. Ve a **Lista Fallecidos**
3. Click en **"Agregar Fallecido"** (se despliega el formulario)
4. Completa los datos:
   - **Datos del Fallecido:** RUT, nombres, apellidos, fecha, ubicación, foto
   - **Ubicación GPS:** Latitud, longitud, link de Google Maps
   - **Historia/Reseña:** Anécdotas o momentos memorables
   - **Familiar Responsable:** Nombre, email, teléfono, parentesco
5. Click en **"Guardar Fallecido"**
6. Aparecerá botón para **enviar WhatsApp** al familiar

### 2. Ver Detalles de un Fallecido

Click en el botón del **ojo** (👁️) para ver:
- Foto grande
- Información completa
- Historia completa
- Datos del familiar
- Botón para ver mapa

### 3. Ver Ubicación en Mapa

Click en el botón del **mapa** (🗺️) para ver:
- Mapa satelital embebido
- Marcador en ubicación exacta
- Botón "Cómo Llegar" para navegación GPS

### 4. Buscar Fallecidos

**Desde la Página Principal:**
- Formulario de búsqueda rápida
- Busca por RUT, nombre o apellidos

**Desde Lista de Fallecidos:**
- Filtros avanzados en la parte superior
- Filtra por fecha, ubicación, etc.

### 5. Exportar a Excel

Desde el Dashboard, click en los botones de exportación para descargar:
- Total de fallecidos
- Registrados hoy
- Por ubicación
- Última semana

## 🛠️ Estructura del Proyecto
```
proyecto_cementerio/
│
├── crudsimple/                    # Aplicación principal
│   ├── models.py                 # Modelo Fallecido
│   ├── views.py                  # Lógica de vistas
│   ├── forms.py                  # Formularios
│   ├── whatsapp_utils.py         # Utilidades WhatsApp
│   └── templates/                # Templates HTML
│       ├── index.html           # Página principal
│       ├── fallecidos.html      # Lista y formulario
│       ├── detalle_fallecido.html  # Detalles completos
│       ├── mapa_tumba.html      # Mapa GPS
│       └── dashboard.html       # Estadísticas
│
├── eva2/                         # Configuración
│   ├── settings.py              # Configuración general
│   └── urls.py                  # Rutas URL
│
├── media/                        # Fotos subidas
│   └── fotos_fallecidos/
│
├── static/                       # Archivos estáticos
│   ├── css/
│   ├── js/
│   └── img/
│
├── db.sqlite3                   # Base de datos
└── manage.py                    # Script Django
```

## 📝 Tecnologías Utilizadas

- **Backend:** Django 5.0
- **Base de Datos:** SQLite
- **Frontend:** HTML5, CSS3, Bootstrap 5.3.3
- **JavaScript:** Vanilla JS
- **Mapas:** Google Maps JavaScript API
- **Validaciones:** Custom RUT validator chileno
- **Exportación:** OpenPyXL
- **Imágenes:** Pillow
- **Íconos:** Font Awesome 5.15.4

## 🐛 Solución de Problemas

### Error: "No module named 'X'"
```bash
pip install nombre_modulo
```

### Las fotos no se muestran
Verifica que en `eva2/urls.py` esté al final:
```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Error de Google Maps
Verifica que la API Key esté correcta en `settings.py` y que hayas habilitado las APIs necesarias.

### Contador "Registrados Hoy" en 0
Ejecuta:
```bash
python manage.py shell
```
```python
from crudsimple.models import Fallecido
from django.utils import timezone
Fallecido.objects.all().update(fecha_registro=timezone.now())
exit()
```

## 📊 Estado del Proyecto

### ✅ Sprints Completados

| Sprint | Estado | Completado |
|--------|--------|-----------|
| Sprint 1: Fundamentos | ✅ | 100% |
| Sprint 2: Motor de Búsqueda | ✅ | 100% |
| Sprint 3: Georreferenciación | ✅ | 100% |
| Sprint 4: Gestión de Usuarios | ✅ | 100% |
| Sprint 5-6: Notificaciones | ⚠️ | 40% (WhatsApp OK, Email pendiente) |
| Sprint 7: Testing/Deploy | ⏳ | Pendiente |

### 🎁 Funcionalidades Extra Implementadas

- Sistema de fotos de fallecidos
- Historia/reseña personalizada
- Página de detalles completos
- Formulario colapsable organizado
- Restricción de fechas automática
- Validación de RUT chileno
- Exportación Excel por categoría

## 🚧 Próximas Mejoras (Opcional)

- [ ] Sistema de emails automáticos
- [ ] Notificaciones programadas con Celery
- [ ] Tests unitarios
- [ ] Deploy en producción
- [ ] App móvil
- [ ] Galería de fotos múltiples
- [ ] Historial de mantenimientos realizados

## 👥 Desarrolladores

- **JaviScript** - Desarrollador Principal
- **Marco** - Colaborador

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

---

**© 2025 Sistema QEPD - Gestión de Cementerios**

*Desarrollado con Django y mucho ☕*