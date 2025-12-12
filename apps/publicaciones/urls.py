# apps/publicaciones/urls.py
from django.urls import path
from . import views
from apps.usuarios.views import registro_usuario 

# Define el "namespace"
app_name = 'publicaciones'

urlpatterns = [
    # Ruta: / (Raíz del sitio) -> Muestra las primeras 8 publicaciones
    path('', views.lista_publicaciones, name='lista'),
    
    # ELIMINAMOS: path('cargar-mas/', views.cargar_mas_publicaciones, name='cargar_mas'),
    
    # Ruta: /articulo/slug-del-articulo/pk/ -> Muestra el artículo completo
    path('articulo/<slug:slug>/<int:pk>/', views.detalle_publicacion, name='detalle'),
    
    # Ruta: /registro/ -> Muestra el formulario de registro
    path('registro/', registro_usuario, name='registro'),
    
    # Ruta: /AcercaDe
    path('acerca/', views.acerca_de, name='acerca'),

    path('categoria/<slug:category_slug>/', views.category_posts, name='category_posts'),
]