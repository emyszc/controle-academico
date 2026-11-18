
from django.core.management import base

from src.models import Curso, Turma


CURSOS = [
    'Técnico em Agropecuária',
    'Técnico em Informática para Internet',
    'Técnico em Administração',
    'Técnico em Mineração',
]

TURMAS = ['A', 'B', 'Única']


class Command(base.BaseCommand):
    def handle(self, *largs, **kwargs):
        for curso in CURSOS:
            Curso.objects.get_or_create(nome=curso)

        for turma in TURMAS:
            Turma.objects.get_or_create(nome=turma)
