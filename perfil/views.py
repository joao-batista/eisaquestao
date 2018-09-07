from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .forms import PerfilForm
from .models import Perfil
from questoes.models import Pergunta

def registrar(request):
    if request.POST:
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            content_type = ContentType.objects.get_for_model(Pergunta)
            permission, created = Permission.objects.get_or_create(
                codename='can_answer_pergunta',
                name='Pode Responder Perguntas',
                content_type=content_type,
            )

            usuario = User.objects.create_user(data.get('login'), data.get('email'), data.get('password'))
            usuario.user_permissions.add(permission)

            perfil = Perfil(login = data.get('login'), email = data.get('email'), imagem = data.get('imagem'), usuario = usuario)
            perfil.save()
    else:
        form = PerfilForm()
    return render(request, 'login_registro.html', { 'form' : form})