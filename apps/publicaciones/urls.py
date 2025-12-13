# apps/publicaciones/urls.py

from django.urls import path
from . import views # Importamos todas las vistas de la aplicación
# NOTA: La vista de registro (registro_usuario) pertenece a la app usuarios, no debe estar aquí.

# Define el "namespace"
app_name = 'publicaciones'

urlpatterns = [
    # 1. HOME / LISTADO GENERAL (Raíz del sitio)
    # Patrón: /
    path('', views.lista_publicaciones, name='lista'),
    
    # 2. LISTADO POR CATEGORÍA
    # Patrón: /categoria/deportes/
    path('categoria/<slug:slug_categoria>/', 
         views.publicaciones_por_categoria, 
         name='por_categoria'),
    
    # 3. CREACIÓN DE PUBLICACIÓN (Colaborador)
    # Patrón: /crear/
    path('crear/', 
         views.PublicacionCrearView.as_view(), 
         name='crear'),
    
    # 4. EDICIÓN DE PUBLICACIÓN (Colaborador)
    # Patrón: /editar/1/
    path('editar/<int:pk>/', 
         views.PublicacionEditarView.as_view(), 
         name='editar'),

    # 5. ELIMINACIÓN DE PUBLICACIÓN (Colaborador)
    # Patrón: /eliminar/1/
    path('eliminar/<int:pk>/', 
         views.PublicacionEliminarView.as_view(), 
         name='eliminar'),
    
    # 6. DETALLE DE PUBLICACIÓN (Nivel 1 y 2)
    # Patrón: /articulo/1/mi-titulo-de-articulo/
    # Usamos PK y slug para URLs SEO-friendly, el PK garantiza unicidad.
    path('articulo/<int:pk>/<slug:slug>/', 
         views.detalle_publicacion, 
         name='detalle'),

    # 7. RUTA ACERCA DE (Función simple)
    # Patrón: /acerca/
    path('acerca/', views.acerca_de, name='acerca'),

    # NOTA IMPORTANTE: La ruta de 'registro' se mantiene en blog_noticias/urls.py 
    # y apunta a la app usuarios. Se omite aquí.
]