from django.shortcuts import render
from django.contrib import messages

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


def calcular_situacao(a):
    if a['docs'] == TOTAL_DOCS and a['biblioteca'] and a['disciplina']:
        return 'apto'
    if a['docs'] == 0:
        return 'incompleto'
    return 'pendente'


def index(request):
    curso = request.GET.get('curso', '')
    turma = request.GET.get('turma', '')
    situacao = request.GET.get('situacao', '')
    busca = request.GET.get('busca', '').strip()

    alunos = [dict(a, situacao=calcular_situacao(a), docs_total=TOTAL_DOCS) for a in ALUNOS]

    resumo = {}
    for s in ('apto', 'pendente', 'incompleto'):
        resumo[s] = sum(1 for a in alunos if a['situacao'] == s)

    if curso:
        alunos = [a for a in alunos if a['curso'] == curso]
    if turma:
        alunos = [a for a in alunos if a['turma'] == turma]
    if situacao:
        alunos = [a for a in alunos if a['situacao'] == situacao]
    if busca:
        b = busca.lower()
        alunos = [a for a in alunos if b in a['nome'].lower() or b in a['matricula']]

    grupos = {}
    for a in alunos:
        chave = (a['curso'], a['turma'])
        if chave not in grupos:
            grupos[chave] = []
        grupos[chave].append(a)

    lista_grupos = []
    for chave, lista in grupos.items():
        lista_grupos.append({'curso': chave[0], 'turma': chave[1], 'alunos': lista})

    opcoes_cursos = []
    for c in sorted({a['curso'] for a in ALUNOS}):
        opcoes_cursos.append({'valor': c, 'sel': c == curso})

    opcoes_turmas = []
    for t in sorted({a['turma'] for a in ALUNOS}):
        opcoes_turmas.append({'valor': t, 'sel': t == turma})

    opcoes_situacao = []
    for v, n in (('apto', 'Apto'), ('pendente', 'Pendente'), ('incompleto', 'Incompleto')):
        opcoes_situacao.append({'valor': v, 'nome': n, 'sel': v == situacao})

    contexto = {
        'grupos': lista_grupos,
        'resumo': resumo,
        'total_exibidos': len(alunos),
        'opcoes_cursos': opcoes_cursos,
        'opcoes_turmas': opcoes_turmas,
        'opcoes_situacao': opcoes_situacao,
        'busca': busca,
    }
    return render(request, 'pendencias/index.html', contexto)