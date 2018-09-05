from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('pergunta/inserir', views.pergunta_inserir, name = 'pergunta_inserir'),
    path('pergunta/atualizar/<int:id>', views.pergunta_atualizar, name = 'pergunta_atualizar'),
]
