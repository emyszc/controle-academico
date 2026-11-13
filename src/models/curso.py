
from django.db import models


class Curso(models.Model):
    nome = models.CharField()
    ativo = models.BooleanField(default=True)

    def curso_turmas(self):
        return self.cursoturma_set.all()
