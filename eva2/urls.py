from django.urls import path
from django.contrib.auth import views as auth_views
from crudsimple import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),

    # Ruta para listar proyectos
    path('fallecidos/', views.listadoFallecidos, name='listadoFallecidos'),

    # Ruta para agregar un proyecto
    path('agregarFallecido/', views.agregarFallecido, name='agregarFallecido'),

    # Ruta para editar un proyecto específico
    path('actualizarFallecido/<int:id>/', views.actualizarFallecido, name='actualizarFallecido'),

    # Ruta para eliminar un proyecto específico
    path('eliminarFallecido/<int:id>/', views.eliminarFallecido, name='eliminarFallecido'),
    path('fallecido/editar/<int:id>/', views.actualizarFallecido, name='actualizarFallecido'),

    # Ruta para el login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
        
    path('buscar-fallecido/', views.buscar_fallecido, name='buscar_fallecido'),
    path('dashboard/', views.dashboard, name='dashboard'),

    
    path('', auth_views.LoginView.as_view(template_name='index.html'), name='logout'),
    

    path('export_total_fallecidos/', views.export_total_fallecidos, name='export_total_fallecidos'),
    path('export_fallecidos_hoy/', views.export_fallecidos_hoy, name='export_fallecidos_hoy'),
    path('export_ubicacion_mas_fallecidos/', views.export_ubicacion_mas_fallecidos, name='export_ubicacion_mas_fallecidos'),
    path('export_fallecidos_ultima_semana/', views.export_fallecidos_ultima_semana, name='export_fallecidos_ultima_semana'),


    path('historias/', views.historias, name='historias'),

    path('sobrenosotros/', views.sobrenosotros, name='sobrenosotros'),
    
    path('mapa/<int:id>/', views.mapa_tumba, name='mapa_tumba'),
    
    path('detalle/<int:id>/', views.detalle_fallecido, name='detalle_fallecido'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)