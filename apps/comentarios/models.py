# apps/comentarios/models.py
from django.db import models
from django.utils import timezone # Importar timezone para la fecha predeterminada
from django.conf import settings 
from apps.publicaciones.models import Publicacion 

class Comentario(models.Model):
    """Modelo para los comentarios de los usuarios."""
    
    # 1. Relación con el usuario (Colega A)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comentarios_autor' # Añadido para evitar conflictos
    )
    
    # 2. Relación con la publicación (Colega B)
    publicacion = models.ForeignKey(
        Publicacion,
        on_delete=models.CASCADE,
        related_name='comentarios' 
    ) 
    
    # 3. Contenido del Comentario (Coincide con el Formulario y la Vista)
    contenido = models.TextField(verbose_name='Comentario') 
    
    # 4. Fecha de Creación (Coincide con la importación de timezone)
    fecha_creacion = models.DateTimeField(default=timezone.now) 
    
    # 5. Campo de Moderación (CRUCIAL para el Admin y la Vista)
    aprobado = models.BooleanField(default=False) 

    class Meta:
        # Ordena del más antiguo al más reciente
        ordering = ['fecha_creacion']

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.publicacion.titulo}"