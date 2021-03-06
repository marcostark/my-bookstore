from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm
import datetime

# Create your views here.

def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    return render(request, 'home.html', data)


def listagem(request):
    data = {}
    #Pegando todas as transações do banco de dados
    data['transacoes'] = Transacao.objects.all() # Manager para manipular banco de dados
    return render(request, 'contas/listagem.html',data)

def nova_transacao(request):
    '''
    :param request:
    :return: form
    Criar um formulario e enviar para o template form.html
    '''
    data = {}
    form = TransacaoForm(request.POST or None)

    # Verificar se o form é valido
    if form.is_valid():
        form.save() # Salva
        return redirect('url_listagem') # E redireciona para a listagem

    data['form'] = form

    return render(request, 'contas/form.html',data)


def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = form = TransacaoForm(request.POST or None, instance=transacao) #Passar o formulario preenchido

    # Verificar se o form é valido
    if form.is_valid():
        form.save()  # Salva
        return redirect('url_listagem')  # E redireciona para a listagem

    data['form'] = form
    data['transacao'] = transacao # Enviando a transação pela URL, para ser possivel remover

    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk) # Buscando o objeto no banco pelo id
    transacao.delete() # Removendo a transação
    return redirect('url_listagem')  # E redireciona para a listagem
