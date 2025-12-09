# apps/usuarios/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Heredamos del formulario estándar de creación de usuarios de Django
class FormularioRegistroUsuario(UserCreationForm):
    class Meta:
        model = User
        # Solo necesitamos username y password (password se maneja automáticamente por UserCreationForm)
        fields = ('username',)
