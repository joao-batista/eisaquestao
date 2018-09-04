from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pergunta_inserir(request):
    return render(request, 'pergunta_form.html')
