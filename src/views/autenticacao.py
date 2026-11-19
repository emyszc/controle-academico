import re

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST


@never_cache
def login(request):

    if request.user.is_authenticated:
        return redirect('biblioteca')

    if request.method == 'POST':

        usuario = request.POST.get('username', '').strip()
        senha = request.POST.get('password', '')

        if not usuario or not senha:
            messages.error(request, 'Preencha todos os campos.')

        else:
            usuario_autenticado = authenticate(
                request,
                username=usuario,
                password=senha
            )

            if usuario_autenticado is not None:

                auth_login(request, usuario_autenticado)

                messages.success(request, 'Login realizado com sucesso!')

                return redirect('biblioteca')

            else:
                messages.error(
                    request,
                    'Usuário ou senha incorretos.'
                )

    return render(request, 'autenticacao/login.html')


def cadastro(request):

    if request.method == 'POST':

        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip().lower()
        usuario = request.POST.get('username', '').strip()
        senha = request.POST.get('password', '')
        confirmar_senha = request.POST.get('confirmar_senha', '')

        if not nome or not email or not usuario or not senha:
            messages.error(request, 'Preencha todos os campos.')

        elif User.objects.filter(first_name__iexact=nome).exists():
            messages.error(request, 'Este nome já está cadastrado.')

        elif User.objects.filter(email__iexact=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')

        elif User.objects.filter(username__iexact=usuario).exists():
            messages.error(request, 'Este login já está sendo utilizado.')

        elif senha.lower() in [nome.lower(), email.lower(), usuario.lower()]:
            messages.error(
                request,
                'A senha não pode ser igual ao nome, e-mail ou login.'
            )

        elif senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')

        elif len(senha) < 8:
            messages.error(
                request,
                'A senha deve possuir pelo menos 8 caracteres.'
            )

        elif not re.search(r'[A-Za-z]', senha):
            messages.error(request, 'A senha deve conter letras.')

        elif not re.search(r'[0-9]', senha):
            messages.error(request, 'A senha deve conter números.')

        elif not re.search(r'[^A-Za-z0-9]', senha):
            messages.error(
                request,
                'A senha deve conter um caractere especial.'
            )

        else:

            novo_usuario = User(
                username=usuario,
                first_name=nome,
                email=email
            )

            try:
                validate_password(senha, user=novo_usuario)

                User.objects.create_user(
                    username=usuario,
                    first_name=nome,
                    email=email,
                    password=senha
                )

                messages.success(
                    request,
                    'Cadastro realizado com sucesso! Faça seu login.'
                )

                return redirect('login')

            except ValidationError as erros:
                for erro in erros:
                    messages.error(request, erro)

    return render(request, 'autenticacao/cadastro.html')


@never_cache
@require_POST
def sair(request):

    logout(request)

    messages.success(
        request,
        'Você saiu do sistema. Faça login novamente.'
    )

    return redirect('login')