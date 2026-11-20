from django.shortcuts import render, redirect
from django.contrib import messages

from src.models import Aluno, Curso, TipoDocumento, Turma

ALUNOS = [
    {'matricula': '2022001', 'nome': 'Ana Beatriz Sousa Lima',  'curso': 'Agropecuária', 'turma': '3º ano A', 'docs': 7, 'biblioteca': True,  'disciplina': True},
    {'matricula': '2022002', 'nome': 'Bruno Henrique Alves',    'curso': 'Agropecuária', 'turma': '3º ano A', 'docs': 2, 'biblioteca': False, 'disciplina': False},
    {'matricula': '2022003', 'nome': 'Carla Eduarda Rodrigues', 'curso': 'Agropecuária', 'turma': '3º ano A', 'docs': 7, 'biblioteca': True,  'disciplina': True},
    {'matricula': '2022004', 'nome': 'Diego Martins Pereira',   'curso': 'Agropecuária', 'turma': '3º ano A', 'docs': 1, 'biblioteca': False, 'disciplina': False},
    {'matricula': '2022007', 'nome': 'Giovana Lopes Melo',      'curso': 'Agropecuária', 'turma': '3º ano B', 'docs': 0, 'biblioteca': True,  'disciplina': False},
    {'matricula': '2022012', 'nome': 'Isabela Ferreira Lima',   'curso': 'Agropecuária', 'turma': '3º ano A', 'docs': 3, 'biblioteca': False, 'disciplina': False},
    {'matricula': '2022022', 'nome': 'Larissa Santos Cruz',     'curso': 'Agropecuária', 'turma': '3º ano A', 'docs': 2, 'biblioteca': False, 'disciplina': True},
    {'matricula': '2022034', 'nome': 'Thiago Nascimento Reis',  'curso': 'Agropecuária', 'turma': '3º ano B', 'docs': 0, 'biblioteca': False, 'disciplina': False},
]

TOTAL_DOCS = 7


def dados_aluno(aluno, docs_total, docs_obrigatorios_total):
    docs_enviados = aluno.documento_set.count()
    docs_obrigatorios_enviados = aluno.documento_set.filter(tipo__obrigatorio=True).count()

    if docs_enviados == docs_total:
        situacao = 'completo'
    elif docs_obrigatorios_enviados == docs_obrigatorios_total:
        situacao = 'apto'
    else:
        situacao = 'pendente'

    resumo_dados = ''
    resumo_dados += ' '.join(map(lambda doc: doc.informacao.lower(), aluno.documento_set.exclude(informacao=None)))
    resumo_dados += ' '.join([aluno.nome.lower(), aluno.email.lower(), aluno.matricula.lower()])

    return {
        'biblioteca': True,
        'curso': aluno.curso_turma.curso.nome,
        'curso_id': str(aluno.curso_turma.curso.id),
        'disciplina': True,
        'docs': docs_enviados,
        'docs_obrigatorios_enviados': docs_obrigatorios_enviados,
        'matricula': aluno.matricula,
        'nome': aluno.nome,
        'situacao': situacao,
        'turma': f'{aluno.curso_turma.ano}º ano - Turma {aluno.curso_turma.turma.nome}',
        'turma_id': str(aluno.curso_turma.turma.id),
        'resumo_dados': resumo_dados,
    }


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    filtros = {}
    ano_selecionado = None
    turma_selecionada = None
    if turma_ano := request.GET.get('turma_ano'):
        if '_' in turma_ano:
            turma_selecionada, ano_selecionado = turma_ano.split('_', 1)

            filtros['curso_turma__ano'] = ano_selecionado
            filtros['curso_turma__turma__nome'] = turma_selecionada

    if id_curso_selecionado := request.GET.get('curso', ''):
        id_curso_selecionado = int(id_curso_selecionado)
        filtros['curso_turma__curso__pk'] = id_curso_selecionado

    if id_turma_selecionada := request.GET.get('turma', ''):
        filtros['curso_turma__turma__pk'] = id_turma_selecionada

    docs_total = TipoDocumento.objects.count()
    docs_obrigatorios_total = TipoDocumento.objects.filter(obrigatorio=True).count()

    alunos = [
        dados_aluno(aluno, docs_total, docs_obrigatorios_total)
        for aluno in Aluno.objects.filter(**filtros)
    ]
    
    if situacao := request.GET.get('situacao', ''):
        alunos = list(filter(lambda aluno: aluno['situacao'] == situacao, alunos))

    if busca := request.GET.get('busca', '').strip():
        alunos = list(filter(lambda aluno: busca.lower() in aluno['resumo_dados'], alunos))

    resumo = {}
    for s in ('completo', 'apto', 'pendente'):
        resumo[s] = sum(1 for a in alunos if a['situacao'] == s)

    grupos = {}
    for aluno in alunos:
        chave = (aluno['curso'], aluno['turma'])
        if chave not in grupos:
            grupos[chave] = []
        grupos[chave].append(aluno)

    lista_grupos = []
    for chave, lista in grupos.items():
        lista_grupos.append({'curso': chave[0], 'turma': chave[1], 'alunos': lista})

    opcoes_situacao = []
    for v, n in (('completo', 'Completo'), ('pendente', 'Pendente'), ('incompleto', 'Incompleto')):
        opcoes_situacao.append({'valor': v, 'nome': n, 'sel': v == situacao})

    contexto = {
        'grupos': lista_grupos,
        'resumo': resumo,
        'total_exibidos': len(alunos),
        'opcoes_situacao': opcoes_situacao,
        'busca': busca,
        'cursos': Curso.objects.all(),
        'turmas': Turma.objects.all(),
        'anos': ['1', '2', '3'],
        'id_curso_selecionado': id_curso_selecionado,
        'ano_selecionado': ano_selecionado,
        'turma_selecionada': turma_selecionada,
    }
    return render(request, 'pendencias/index.html', contexto)