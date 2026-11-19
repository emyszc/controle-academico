from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib import messages
from src.models import Aluno, Curso, Turma
from src.forms import CursoTurmaForm


def contexto_basico_curso(codigo_curso):
    contexto = {
        'anos': [1, 2, 3]
    }

    if curso := Curso.objects.filter(codigo=codigo_curso).first():
        contexto['curso'] = curso
        contexto['cursos_turmas_por_ano'] = {}
        contexto['turmas_totais'] = 0

        for ano in contexto['anos']:
            contexto['cursos_turmas_por_ano'][ano] = curso.cursoturma_set.filter(ano=ano).order_by('turma__nome')
            contexto['turmas_totais'] += contexto['cursos_turmas_por_ano'][ano].count()

            for curso_turma in contexto['cursos_turmas_por_ano'][ano]:
                curso_turma.alunos = Aluno.objects.filter(curso_turma=curso_turma).order_by('nome')
                curso_turma.total_alunos = curso_turma.alunos.count()

    return contexto


def cursos(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        turma_id = request.POST.get('turma')
        curso_id = request.POST.get('curso')
        ano = request.POST.get('ano')

        form = CursoTurmaForm({
            'turma': turma_id,
            'curso': curso_id,
            'ano': ano
        })

        if form.is_valid():
            messages.success(request, 'Cadastro realizado com sucesso!')
            form.save()
        else:
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, error)
    contexto = {
        'anos': [1, 2, 3],
        'cursos': Curso.objects.all(),
        'turmas': Turma.objects.all(),
        'quantidade_turmas_por_curso': {},
        'quantidade_alunos_por_curso': {},
    }

    for curso in contexto['cursos']:
        contexto['quantidade_turmas_por_curso'][curso.codigo] = curso.curso_turmas().count()
        contexto['quantidade_alunos_por_curso'][curso.codigo] = curso.alunos().count()

    return render (request, 'cursos/cursos.html', contexto)

def curso(request, codigo):
    if not request.user.is_authenticated:
        return redirect('login')

    contexto = contexto_basico_curso(codigo)

    if contexto['curso']:
        return render(request, 'cursos/curso.html', contexto)

    return HttpResponseNotFound()

def login(request):
    print(f'Dados recebidos: {request.GET}')
    return render (request, 'cursos/cursos.html')
