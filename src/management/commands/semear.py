
from django.core.management import base

from src.models import Curso, Turma


CURSOS = [
    { 'nome': 'Técnico em Administração',             'codigo': 'ADM'  },
    { 'nome': 'Técnico em Agropecuária',              'codigo': 'AGRO' },
    { 'nome': 'Técnico em Informática para Internet', 'codigo': 'INFO' },
    { 'nome': 'Técnico em Mineração',                 'codigo': 'MIN'  },
]

TURMAS = ['A', 'B', 'Única']


class Command(base.BaseCommand):
    def handle(self, *largs, **kwargs):
        print('\nCriando cursos...')
        for curso in CURSOS:
            print(f'Criando curso {curso["nome"]}...', end=' ')
            Curso.objects.get_or_create(nome=curso['nome'], codigo=curso['codigo'])
            print('CRIADO!')
        print('Cursos criados!')

        print('\nCriando turmas...')
        for turma in TURMAS:
            print(f'Criando turma {turma}...', end=' ')
            Turma.objects.get_or_create(nome=turma)
            print('CRIADA!')
        print('Turmas criadas!')

