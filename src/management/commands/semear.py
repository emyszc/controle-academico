
from django.core.management import base
from django.contrib.auth import hashers, models

from src.models import Curso, Turma, TipoDocumento


CURSOS = [
    { 'nome': 'Técnico em Administração',             'codigo': 'ADM'  },
    { 'nome': 'Técnico em Agropecuária',              'codigo': 'AGRO' },
    { 'nome': 'Técnico em Informática para Internet', 'codigo': 'INFO' },
    { 'nome': 'Técnico em Mineração',                 'codigo': 'MIN'  },
]

TIPOS_DOCUMENTOS = [
    { 'nome': 'RG',                              'obrigatorio':  True, 'arquivo_obrigatorio': False },
    { 'nome': 'CPF',                             'obrigatorio':  True, 'arquivo_obrigatorio': False },
    { 'nome': 'Comprovante de Residência',       'obrigatorio':  True, 'arquivo_obrigatorio': False },
    { 'nome': 'Conclusão de Ensino Fundamental', 'obrigatorio':  True, 'arquivo_obrigatorio': False },
    { 'nome': 'Histórico Escolar',               'obrigatorio':  True, 'arquivo_obrigatorio': False },
    { 'nome': 'Foto 3x4',                        'obrigatorio': False, 'arquivo_obrigatorio':  True },
    { 'nome': 'Certidão de Nascimento',          'obrigatorio': False, 'arquivo_obrigatorio': False },
    { 'nome': 'Quitação Eleitoral',              'obrigatorio': False, 'arquivo_obrigatorio': False },
    { 'nome': 'Quitação Militar',                'obrigatorio': False, 'arquivo_obrigatorio': False },
]

TURMAS = ['A', 'B', 'Única']

USUARIOS: list[dict[str, str]] = [
    { 'username': 'servidor.academico', 'password': 'ifpi@2025', 'first_name': 'Servidor', 'last_name': 'Acadêmico' },
]


class Command(base.BaseCommand):
    def handle(self, *largs, **kwargs):
        print('\nCriando usuários...')
        for dados_usuario in USUARIOS:
            print(f'Criando usuário {dados_usuario["first_name"]} {dados_usuario["last_name"]} ({dados_usuario["username"]})...', end=' ')
            dados_usuario['password'] = hashers.make_password(dados_usuario['password'])
            username = dados_usuario.pop('username')
            models.User.objects.get_or_create(dados_usuario, username=username)
            print('CRIADO!')
        print('Usuários criados!')

        print('\nCriando cursos...')
        for curso in CURSOS:
            print(f'Criando curso {curso["nome"]}...', end=' ')
            Curso.objects.get_or_create(nome=curso['nome'], codigo=curso['codigo'])
            print('CRIADO!')
        print('Cursos criados!')

        print('\nCriando turmas...')
        for turma in TURMAS:
            print(f'Criando turma {turma}...', end=' ')
            Turma.objects.get_or_create(nome=turma)
            print('CRIADA!')
        print('Turmas criadas!')

        print('\nCriando tipos de documentos...')
        for tipo_documento in TIPOS_DOCUMENTOS:
            print(f'Criando Tipo de Documento {tipo_documento["nome"]}...', end=' ')
            nome = tipo_documento.pop('nome')
            TipoDocumento.objects.get_or_create(tipo_documento, nome=nome)
            print('Criado!')
        print('Tipos de Documentos criados!')
