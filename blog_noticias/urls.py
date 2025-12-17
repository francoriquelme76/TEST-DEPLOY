# blog_noticias/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. URLs de la aplicación USUARIOS (REGISTRO)
    path('cuentas/', include('apps.usuarios.urls', namespace='usuarios')), 
    
    #2 Login personalizado para redireccion de usuarios logueados
    path('cuentas/login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    # 3. LOGOUT, PASSWORD RESET, etc.
    path('cuentas/', include('django.contrib.auth.urls')),
    
    # 4. URLs de la aplicación COMENTARIOS
    path('comentarios/', include('apps.comentarios.urls', namespace='comentarios')),
    
    # 5. URLs de publicaciones (Home)
    path('', include('apps.publicaciones.urls')),
]

# Configuración para servir archivos MEDIA y STATIC durante el desarrollo (DEBUG=True)
if settings.DEBUG:
    # Si usas archivos subidos por el usuario (imágenes de publicaciones, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Los archivos STATIC ya suelen ser servidos por runserver, 
    # pero esta línea es útil si tienes configuraciones específicas.
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)