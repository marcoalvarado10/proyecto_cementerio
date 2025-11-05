# 🏛️ Sistema de Administración de Cementerio

Sistema web para gestión de fallecidos con notificaciones WhatsApp.

## 🚀 Instalación Rápida

### 1. Instalar dependencias (copiar todo de una vez)
```bash
pip install django pymysql openpyxl cryptography
```

### 2. Configurar base de datos (copiar todo de una vez)
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser


```

Cuando pida datos:
- Username: admin (o el que quieras)
- Email: (presiona Enter)
- Password: (escribe tu contraseña)



### 3. Iniciar servidor
```bash
python manage.py runserver
```

## 🌐 Acceso

Abre: **http://127.0.0.1:8000/login/**

Usuario y contraseña: los que creaste en el paso 2

## ✨ Características

✅ Validación RUT chileno  
✅ WhatsApp automático  
✅ Dashboard estadísticas  
✅ Búsqueda avanzada  
✅ Fechas mantenimiento  
✅ Export Excel  

## 🛑 Detener

Presiona `Ctrl+C`

---

**© 2025**