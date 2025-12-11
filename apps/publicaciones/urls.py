# apps/publicaciones/urls.py (Versión Corregida)
from django.urls import path
from . import views

# Define el "namespace" de la aplicación para evitar conflictos de nombres
app_name = 'publicaciones'

urlpatterns = [
    # Ruta: / (Raíz del sitio) -> Muestra todas las publicaciones
    path('', views.lista_publicaciones, name='lista'),
    
    # Ruta: /articulo/slug-del-articulo/ -> Muestra el artículo completo
    path('articulo/<slug:slug>/<int:pk>/', views.detalle_publicacion, name='detalle'),
    
    # 🚨 NUEVA RUTA DE CREACIÓN (Implementación que hicimos en el paso anterior) 🚨
    # Ruta: /crear/ -> Muestra el formulario para crear una nueva publicación
    path('crear/', views.PublicacionCrearView.as_view(), name='crear'),
]
