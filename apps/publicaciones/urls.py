# apps/publicaciones/urls.py
from django.urls import path
from . import views
from apps.usuarios.views import registro_usuario # ¡IMPORTAR LA NUEVA VISTA!

# Define el "namespace" de la aplicación para evitar conflictos de nombres
app_name = 'publicaciones'

urlpatterns = [
    # Ruta: / (Raíz del sitio) -> Muestra todas las publicaciones
    path('', views.lista_publicaciones, name='lista'),
    
    # Ruta: /articulo/slug-del-articulo/ -> Muestra el artículo completo
    path('articulo/<slug:slug>/<int:pk>/', views.detalle_publicacion, name='detalle'),
    
    # ¡NUEVA RUTA DE REGISTRO!
    # Ruta: /registro/ -> Muestra el formulario de registro
    path('registro/', registro_usuario, name='registro'),
]
