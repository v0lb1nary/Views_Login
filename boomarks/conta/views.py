from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import ClienteForm
from .models import Cliente
from django.contrib.auth.decorators import login_required

@login_required
def painel_controle(request):
    return render(request, 'conta/painel_controle.html', {'section':'painel_controle'})


def cadastro(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return HttpResponse('Cadastrado com Sucesso ')
    else:
        formulario = ClienteForm()

    return render(request, 'conta/cadastro.html', {'formulario': formulario})


# def login_usuario(request):
#     if request.method == 'POST':
#         formulario = FormularioLogin(request.POST)
#         if formulario.is_valid():
#             cd = formulario.cleaned_data
#             user = authenticate(request, 
#                                 username = cd['nome_usuario'],
#                                 password = cd['senha'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Autenticado ' 'Sucesso')
#                 else:
#                     return HttpResponse('Conta está desativada')
#             else:
#                 return HttpResponse('Login Inválido')
#     else:
#         formulario = FormularioLogin()

#     return render(request, 'conta/login.html', {'formulario':formulario})

