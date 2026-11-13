from django.shortcuts import render
from src.models import Curso, Turma, CursoTurma

ANOS = [1, 2, 3]

TURMAS = ['A', 'B', 'Turma Única']

CURSOS = [
    {
        'nome': 'Técnico em Agropecuária',
        'turmas': [
            {'nome': '3º ANO A', 'alunos': 6},
            {'nome': '3º ANO B', 'alunos': 2},
        ],
        'alunos': 8,
    },
    {
        'nome': 'Técnico em Informática para Internet',
        'turmas': [
            {'nome': '3º ANO A', 'alunos': 5},
            {'nome': '3º ANO B', 'alunos': 4},
        ],
        'alunos': 9,
    },
    {
        'nome': 'Técnico em Administração',
        'turmas': [
            {'nome': '3º ANO A', 'alunos': 7},
            {'nome': '3º ANO B', 'alunos': 3},
        ],
        'alunos': 10,
    },
]

def cursos(request):
    contexto = {
        'cursos': Curso.objects.all(),
        'anos': ANOS,
        'turmas': Turma.objects.all(),
    }

    if request.method == 'GET':
        return render (request, 'cursos/cursos.html', contexto)

    if request.method == 'POST':
        turma_id = request.POST.get('turma')
        curso_id = request.POST.get('curso')
        ano = request.POST.get('ano')

        CursoTurma.objects.create(turma_id=turma_id, curso_id=curso_id)

        return render (request, 'cursos/cursos.html', contexto)

def login(request):
    print(f'Dados recebidos: {request.GET}')
    return render (request, 'cursos/cursos.html')
