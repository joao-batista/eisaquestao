from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('pergunta/inserir', views.pergunta_inserir, name = 'pergunta_inserir'),
    path('pergunta/atualizar/<int:id>', views.pergunta_atualizar, name = 'pergunta_atualizar'),
    path('filtrar/', views.filtrar, name = 'filtrar'),
    path('responder_ajax/', views.responder_ajax, name='responder_ajax'),
    path('publicar_ajax/', views.publicar_ajax, name='publicar_ajax'),
]
