# publicaciones/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Eliminamos la importación de JsonResponse
from .models import Publicacion, Categoria

# Importaciones para comentarios:
from apps.comentarios.forms import ComentarioForm
from apps.comentarios.models import Comentario 


# 1. Vista para la lista de publicaciones (Función SIMPLIFICADA)
def lista_publicaciones(request):
    """
    Obtiene las primeras 8 publicaciones y las muestra en la página de inicio.
    """
    print("¡VISTA LLAMADA Y A PUNTO DE RENDERIZAR!")
    # Tomamos SOLO 8 publicaciones para mostrar en la pantalla de inicio
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')[:8]
    
    contexto = {
        'object_list': publicaciones,
        'titulo': 'Blog de Noticias',
        # Eliminamos 'hay_mas' y 'offset_inicial'
    }
    
    return render(request, 'publicaciones/lista_publicaciones.html', contexto) 


# 2. Vista para el detalle de un artículo (Función con lógica de Comentarios)
@login_required 
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
            
            # Guardar el comentario 
            nuevo_comentario.save()
            
            # Redirigir
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

# 3. renderizar página  "Acerca De"
def acerca_de(request):
    """Renderiza el template estático AcercaDe.html."""
    return render(request, 'AcercaDe.html')

# 4. Filtro para las Categorías (category_posts)
def category_posts(request, category_slug):
    """
    Filtra y lista todas las publicaciones que pertenecen a una categoría específica.
    """
    # 1. Obtiene el objeto Categoria usando el slug de la URL
    categoria = get_object_or_404(Categoria, slug=category_slug)
    
    # 2. Filtra las publicaciones. 
    #    Usamos 'categoria=categoria' porque el campo ForeignKey en Publicacion se llama 'categoria'.
    publicaciones_filtradas = Publicacion.objects.filter(categoria=categoria).order_by('-fecha_creacion')

    contexto = {
        # Usamos el mismo nombre de variable que en lista_publicaciones.
        'object_list': publicaciones_filtradas, 
        'titulo': f'Publicaciones en: {categoria.nombre}', 
        'current_category': categoria.nombre 
    }
    
    # Reutiliza el template de lista
    return render(request, 'publicaciones/lista_publicaciones.html', contexto)