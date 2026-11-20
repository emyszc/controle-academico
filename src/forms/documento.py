
from django import forms

from src.models import Documento


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ('informacao', 'arquivo', 'tipo')


