
from django.db import models

class TipoDocumento(models.Model):
    nome = models.CharField()
    obrigatorio = models.BooleanField()
    arquivo_obrigatorio = models.BooleanField()
