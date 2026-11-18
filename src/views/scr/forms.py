from django import forms

OPCOES_DOCUMENTOS = [
    ("RG"),
    ("CPF"),
    ("Certidão de Nascimento"),
    ("Foto 3x4"),
    ("Comprovante de Residência"),
    ("Quitação Eleitoral"),
    ("Quitação Militar"),
    ("Conclusão de Ensino Fundamental"),
    ("Histórico Escolar")
]

class DocumentosForm(forms.Form):
    declaracao = forms.BooleanField(
        required=True
    )

    documentos = forms.MultipleChoiceField(
        choices=OPCOES_DOCUMENTOS,
        widget=forms.CheckboxSelectMultiple,
        label="Selecione os documentos apresentados",
        required=False
    )