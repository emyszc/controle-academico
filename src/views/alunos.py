
from django.shortcuts import render


def aluno(request):
    return render(request, 'alunos/aluno.html')

