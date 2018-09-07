from django import template
from questoes.models import Respondida, Perfil, Pergunta

register = template.Library()

@register.filter
def number_to_char(key):
    alternativas = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e'}
    return alternativas.get(key)


@register.simple_tag
def feedback(*args, **kwargs):
    perfil = kwargs['perfil']
    pergunta = kwargs['pergunta']
    div = kwargs['div']

    try:
        respondida = Respondida.objects.get(perfil=perfil, pergunta=pergunta)
        correta = respondida.alternativa.correta
        if correta and div == 'is_correta':
            return 'show'
        elif correta and div == 'is_incorreta':
            return 'hide'
        elif not correta and div == 'is_correta':
            return 'hide'
        elif not correta and div == 'is_incorreta':
            return 'show'
    except Exception:
        return 'hide'
