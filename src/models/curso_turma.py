
from django.db import models

class CursoTurma(models.Model):
    ano = models.IntegerField()
    turma = models.ForeignKey('Turma', on_delete=models.PROTECT)
    curso = models.ForeignKey('Curso', on_delete=models.PROTECT)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['ano', 'turma_id', 'curso_id'],
                name='curso_turma_ano',
            )
        ]
