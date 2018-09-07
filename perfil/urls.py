from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.registrar, name = 'registrar'),
    path('login/', auth_views.LoginView.as_view(template_name='login_registro.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login_registro.html'), name='logout'),
]
