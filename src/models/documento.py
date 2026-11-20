
from django.conf import settings
from django.db import models


def caminho_documento_aluno(documento, nome_arquivo):
    return f'{documento.aluno.id}/{nome_arquivo}'


class Documento(models.Model):
    aluno = models.ForeignKey('Aluno', models.PROTECT)
    tipo = models.ForeignKey('TipoDocumento', models.PROTECT)
    informacao = models.CharField(blank=True, null=True)
    arquivo = models.FileField(upload_to=caminho_documento_aluno, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True, blank=True, related_name='%(class)s_criados')
    modificado_por = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')
