from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome Completo")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    matricula = models.CharField(max_length=20, unique=True, verbose_name="Matrícula")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    ativo = models.BooleanField(default=True, verbose_name="Matrícula Ativa")
    criado_em = models.DateTimeField(auto_now_add=True)
    curso_turma = models.ForeignKey('CursoTurma', models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
   
