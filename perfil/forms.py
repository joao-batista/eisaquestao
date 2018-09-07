from django.forms import ModelForm, ValidationError, TextInput
from django.contrib.auth.models import User
from .models import Perfil
import re

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['login', 'email', 'password', 'imagem']

    def clean(self):
        usuario_existe = User.objects.filter(username=self.cleaned_data['login']).exists()
        if usuario_existe:
            raise ValidationError('Usuário já existe')
        if not re.match("^[a-zA-Z0-9_.-]+$", self.cleaned_data['login']):
            raise ValidationError('login inválido')
        return self.cleaned_data