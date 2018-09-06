from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    imagem = models.ImageField(upload_to='imagens/', default = 'imagens/no-img.jpg')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
