
from django.forms import models, fields

from src.models import CursoTurma


class CursoTurmaForm(models.ModelForm):
    class Meta:
        model = CursoTurma
        fields = '__all__'