# apps/comentarios/admin.py
from django.contrib import admin
from .models import Comentario # Importamos el modelo

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    # Columnas que se mostrarán en la lista de comentarios
    list_display = ('autor', 'publicacion', 'fecha_creacion', 'aprobado')
    
    # Filtros laterales para ver comentarios aprobados vs. pendientes
    list_filter = ('aprobado', 'fecha_creacion')
    
    # Acciones rápidas para moderación masiva
    actions = ['aprobar_comentarios', 'desaprobar_comentarios']

    def aprobar_comentarios(self, request, queryset):
        """Marca una selección de comentarios como aprobados."""
        queryset.update(aprobado=True)
    aprobar_comentarios.short_description = "Marcar comentarios seleccionados como Aprobados"

    def desaprobar_comentarios(self, request, queryset):
        """Marca una selección de comentarios como pendientes de aprobación."""
        queryset.update(aprobado=False)
    desaprobar_comentarios.short_description = "Marcar comentarios seleccionados como Pendientes"
