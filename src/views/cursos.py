from django.shortcuts import render

CURSOS = [
    {
        'nome': 'Agropecuária',
        'turmas': [
            {'nome': '3º ano A', 'alunos': 6},
            {'nome': '3º ano B', 'alunos': 2},
        ],
        'alunos': 8,
    },
    {
        'nome': 'Informática',
        'turmas': [
            {'nome': '3º ano A', 'alunos': 5},
            {'nome': '3º ano B', 'alunos': 4},
        ],
        'alunos': 9,
    },
    {
        'nome': 'Administração',
        'turmas': [
            {'nome': '3º ano A', 'alunos': 7},
            {'nome': '3º ano B', 'alunos': 3},
        ],
        'alunos': 10,
    },
]

def cursos (request):
    contexto = {
        'cursos': CURSOS
    }

    return render (request, 'cursos/cursos.html', contexto)
