
from django.db import models

from .aluno import Aluno


class Curso(models.Model):
    nome = models.CharField()
    codigo = models.CharField()
    ativo = models.BooleanField(default=True)

    def curso_turmas(self):
        return self.cursoturma_set.all()

    def alunos(self):
        return Aluno.objects.filter(curso_turma__curso_id=self.pk)
