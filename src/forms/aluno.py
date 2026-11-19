
from django import forms

from src.models import Aluno, CursoTurma


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('nome', 'email', 'matricula', 'data_nascimento', 'curso_turma')

    def clean(self):
        data = super().clean()

        if curso_turma_id := self.data.get('curso_turma', None):
            if curso_turma := CursoTurma.objects.filter(pk=curso_turma_id).first():
                data['curso_turma'] = curso_turma

        if not data.get('curso_turma'):
            self.add_error('curso_turma', 'Este campo é obrigatório.')

        return data

    def save(self, commit = True):
        self.instance.curso_turma = self.cleaned_data['curso_turma']

        return super().save(commit)
