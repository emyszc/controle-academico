
from django.db import models

class CursoTurma(models.Model):
    turma = models.ForeignKey('Turma', on_delete=models.PROTECT)
    curso = models.ForeignKey('Curso', on_delete=models.PROTECT)
