from django.shortcuts import render, get_object_or_404, redirect # Importar 'redirect'
from django.contrib.auth.decorators import login_required # Para requerir autenticación en comentarios
from .models import Publicacion, Categoria
# Importaciones para comentarios:
from apps.comentarios.forms import ComentarioForm
from apps.comentarios.models import Comentario 


# 1. Vista para la lista de publicaciones (Función)
def lista_publicaciones(request):
    """
    Obtiene todas las publicaciones y las muestra en la página de inicio.
    """
    publicaciones = Publicacion.objects.all()
    
    contexto = {
        'object_list': publicaciones,
        'titulo': 'Blog de Noticias',
    }
    
    # ¡Línea faltante! Esto renderiza el HTML:
    return render(request, 'publicaciones/lista_publicaciones.html', contexto) 


# 2. Vista para el detalle de un artículo (Función con lógica de Comentarios)
@login_required # El usuario debe iniciar sesión para acceder al detalle y comentar
def detalle_publicacion(request, pk, slug):
    # Obtener la publicación (si no existe, retorna 404)
    publicacion = get_object_or_404(
        Publicacion, 
        pk=pk, 
        slug=slug
    )
    
    # Obtener solo los comentarios aprobados de esta publicación
    comentarios = publicacion.comentarios.filter(aprobado=True)
    
    nuevo_comentario = None
    if request.method == 'POST':
        # Procesar el formulario enviado (POST)
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():
            # Crear el objeto comentario, pero aún sin guardar en la BD
            nuevo_comentario = comentario_form.save(commit=False)
            
            # Asignar la publicación y el autor (usuario logueado)
            nuevo_comentario.publicacion = publicacion
            nuevo_comentario.autor = request.user
            
            # Guardar el comentario (ahora sí, con todos los campos obligatorios)
            nuevo_comentario.save()
            
            # Redirigir para evitar que el comentario se envíe dos veces
            return redirect('publicaciones:detalle', pk=publicacion.pk, slug=publicacion.slug)
    else:
        # Mostrar el formulario vacío (GET)
        comentario_form = ComentarioForm()
    
    contexto = {
        'publicacion': publicacion,
        'comentarios': comentarios,           
        'comentario_form': comentario_form,
    }
    
    return render(request, 'publicaciones/detalle_publicacion.html', contexto)