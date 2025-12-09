# apps/usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login # Importar la función login para iniciar sesión automáticamente
from .forms import FormularioRegistroUsuario # Importaremos este formulario en el siguiente paso

# Vista para manejar el registro de nuevos usuarios
def registro_usuario(request):
    if request.method == 'POST':
        # Procesar los datos enviados por el usuario
        form = FormularioRegistroUsuario(request.POST)
        if form.is_valid():
            # Guardar el nuevo usuario en la base de datos
            user = form.save()
            # Iniciar sesión automáticamente al nuevo usuario
            login(request, user)
            # Redirigir a la página de inicio
            return redirect('publicaciones:lista') # Asumiendo que 'lista' es el nombre de tu URL principal
    else:
        # Mostrar el formulario vacío si es una petición GET
        form = FormularioRegistroUsuario()
        
    return render(request, 'usuarios/registro.html', {'form': form})
