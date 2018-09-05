from django import template

register = template.Library()

@register.filter
def number_to_char(key):
    alternativas = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e'}
    return alternativas.get(key)