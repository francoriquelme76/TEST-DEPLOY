# blog_noticias/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 
# Nota: Ya no necesitamos from apps.usuarios import urls as usuarios_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. URLs de la aplicación USUARIOS (REGISTRO)
    # Patrón: /cuentas/registro/
    path('cuentas/', include('apps.usuarios.urls', namespace='usuarios')), 

    # 2. LOGIN (Forzamos la plantilla que debe usar)
    # Patrón: /accounts/login/
    path('accounts/login/', 
         auth_views.LoginView.as_view(template_name='registration/login.html'), 
         name='login'),
    
    # 3. LOGOUT (Forzamos la plantilla que debe usar)
    # Patrón: /accounts/logout/
    path('accounts/logout/', 
         auth_views.LogoutView.as_view(template_name='registration/logout.html'), 
         name='logout'), 
    
    # 4. URLs de publicaciones
    path('', include('apps.publicaciones.urls')),
    
    # IMPORTANTE: Aquí se incluirían las URLs de restablecimiento de contraseña (password reset),
    # pero las omitimos para simplificar si no las estás usando.
    # Si las necesitas: path('accounts/', include('django.contrib.auth.urls')), PERO SIN LOGIN NI LOGOUT EXPLICITOS
]
