from django.shortcuts import render, redirect
from .forms import PerguntaForm, AlternativaForm, FiltroForm
from .models import Pergunta, Alternativa, Respondida, Comentario
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    perguntas = Pergunta.objects.all()
    return render_index(request, perguntas)

@permission_required('questoes.add_pergunta', raise_exception=True)
def pergunta_inserir(request):
    form_pergunta = PerguntaForm(request.POST)
    form_alternativas = [AlternativaForm(request.POST, prefix = str(i)) for i in range(1, 6)]

    if (form_pergunta.is_valid() and all(form_alternativa.is_valid() for form_alternativa in form_alternativas)):
        pergunta = form_pergunta.save()
        for form_alternativa in form_alternativas:
            alternativa = form_alternativa.save(commit=False)
            alternativa.pergunta = pergunta
            alternativa.save()
        redirect('index')
    return render(request, 'pergunta_form.html', { 'form_pergunta' : form_pergunta,  'form_alternativas': form_alternativas })

@permission_required('questoes.change_pergunta', raise_exception=True)
def pergunta_atualizar(request, id):
    pergunta = Pergunta.objects.get(pk = id)
    form_pergunta = PerguntaForm(request.POST or None, instance = pergunta)
    form_alternativas = [AlternativaForm(request.POST or None, instance = alternativa, prefix = str(alternativa.id)) for alternativa in pergunta.alternativa.all()]

    if (form_pergunta.is_valid() and all(form_alternativa.is_valid() for form_alternativa in form_alternativas)):
        form_pergunta.save()
        for form_alternativa in form_alternativas:
            form_alternativa.save()
        redirect('index')
    return render(request, 'pergunta_form.html', { 'form_pergunta' : form_pergunta,  'form_alternativas': form_alternativas })


def filtrar(request):
    form = FiltroForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        query = Q()
        if data.get('disciplina'):
            query.add(Q(disciplina = data.get('disciplina')), Q.AND)
        if data.get('banca'):
            query.add(Q(banca = data.get('banca')), Q.AND)
        if data.get('ano'):
            query.add(Q(ano = data.get('ano')), Q.AND)
        if data.get('nivel'):
            query.add(Q(nivel = data.get('nivel')), Q.AND)
        if data.get('orgao'):
            query.add(Q(orgao = data.get('orgao')), Q.AND)
        perguntas = Pergunta.objects.filter(query).all()
    return render_index(request, perguntas)

def responder_ajax(request):
    id = request.POST.get('id')
    alternativa = Alternativa.objects.get(pk = id)
    pergunta = alternativa.pergunta
    perfil = request.user.perfil

    try:
        respondida = Respondida.objects.get(pergunta = pergunta, perfil = perfil)
        respondida.alternativa = alternativa
        respondida.save()
    except Respondida.DoesNotExist:
        Respondida.objects.create(pergunta = pergunta, perfil = perfil, alternativa = alternativa)
    return JsonResponse({'resposta' : alternativa.correta})

def publicar_ajax(request):
    id = request.POST.get('id')
    texto = request.POST.get('texto')
    pergunta = Pergunta.objects.get(pk = id)
    perfil = request.user.perfil

    try:
        comentario = Comentario.objects.get(pergunta = pergunta, perfil = perfil)
        comentario.texto = texto
        comentario.save()
    except Comentario.DoesNotExist:
        Comentario.objects.create(pergunta = pergunta, perfil = perfil, texto = texto)
    return JsonResponse({'resposta' : texto})

def render_index(request, perguntas):
    paginator = Paginator(perguntas, 5)

    page = request.GET.get('page')
    perguntas = paginator.get_page(page)

    return render(request, 'index.html', { 'perguntas' : perguntas, 'filtro_form' : FiltroForm() })