# blog_noticias/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # ¡Necesitas esta importación!

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ESTA LÍNEA DEBE SER LA ÚNICA QUE MANEJE EL LOGOUT
    path('accounts/logout/', auth_views.LogoutView.as_view(
        template_name='registration/logout.html'), name='logout'), 
    
    # El resto de la autenticación
    path('accounts/', include('django.contrib.auth.urls')), 
    
    path('', include('apps.publicaciones.urls')),
]