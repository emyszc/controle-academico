
from django.shortcuts import render


def login(request):
    return render(request, 'autenticacao/login.html')

def login(request):
    print(f'Dados recebidos: {request.GET}')
    return render (request, 'autenticacao/login.html')