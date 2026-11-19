
from django import template


register = template.Library()


@register.filter
def na_posicao(valores, posicao):
    return valores[posicao]

