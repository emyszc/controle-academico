from django.shortcuts import render

ANOS = ['1º ANO', '2º ANO', '3º ANO']

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

def cursos (request):
    contexto = {
        'cursos': CURSOS,
        'anos': ANOS,
        'turmas': TURMAS,
    }

    return render (request, 'cursos/cursos.html', contexto)

def login(request):
    print(f'Dados recebidos: {request.GET}')
    return render (request, 'cursos/cursos.html')
