
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from src.forms import AlunoForm, DocumentoForm
from src.models import Aluno, Documento, TipoDocumento
from src.views.cursos import contexto_basico_curso


def aluno_documentos(matricula=None, aluno=None):
    documentos = []

    if not aluno:
        aluno = Aluno.objects.filter(matricula=matricula).first()

    if aluno:
        documentos = []

        for tipo_documento in TipoDocumento.objects.all():
            if documento := aluno.documento_set.filter(tipo=tipo_documento).first():
                documentos.append(DocumentoForm(instance=documento))
            else:
                documento = Documento(tipo=tipo_documento)
                documentos.append(DocumentoForm(instance=documento))

    return aluno, documentos

def aluno(request, matricula):
    if not request.user.is_authenticated:
        return redirect('login')

    aluno, documentos = aluno_documentos(matricula)

    if aluno:
        return render(request, 'alunos/aluno.html', { 'aluno': aluno, 'documentos': documentos })

    return HttpResponseNotFound()


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


def enviar_documento(request, matricula):
    if not request.user.is_authenticated:
        return redirect('login')

    if aluno := Aluno.objects.filter(matricula=matricula).first():
        tipo_documento_id = request.POST.get('tipo')

        if documento := Documento.objects.filter(aluno=aluno, tipo__pk=tipo_documento_id).first():
            form = DocumentoForm(request.POST, request.FILES, instance=documento)
        else:
            form = DocumentoForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.aluno = aluno
            form.save()
        else:
            if form.errors:
                for campo, erros in form.errors.items():
                    for erro in erros:
                        messages.error(campo, f'[{campo}] {erro}')

        _, documentos = aluno_documentos(aluno=aluno)

        return render(request, 'alunos/aluno.html', { 'aluno': aluno, 'documentos': documentos })

    return HttpResponseNotFound()
