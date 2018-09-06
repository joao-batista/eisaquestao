from django.shortcuts import render


def registrar(request):
    return render(request, 'login_registro.html')