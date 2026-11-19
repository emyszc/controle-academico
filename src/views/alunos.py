
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from src.forms import AlunoForm
from src.views.cursos import contexto_basico_curso


def aluno(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'alunos/aluno.html')


def cadastrar_aluno(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        contexto = contexto_basico_curso(request.POST.get('codigo_curso'))

        contexto['form'] = AlunoForm(request.POST)

        if contexto['form'].is_valid() and contexto['curso']:
            contexto['form'].save()
            messages.success(request, 'Aluno cadastrado com sucesso!')
        else:
            for campo, erros in contexto['form'].errors.items():
                for erro in erros:
                    messages.error(request, f'[{campo}] {erro}')

        return render(request, 'cursos/curso.html', contexto)

    return HttpResponseNotFound()

