#agenda/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Contato
from .forms import ContatoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm # Importe o formulário de criação de usuário

#Biblioteca para escrever codigo html diretamente da view
from django.http import HttpResponse

@login_required()
def contato_lista(request):
    contatos = Contato.objects.filter(user=request.user)
    return render(request,
                  'agenda/contato_lista.html',
                  {'contatos' : contatos})

@login_required()
def contato_criar(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES)
        if form.is_valid():
            #salva os dados do form, mas nao grava no banco de dados
            contato = form.save(commit=False)
            contato.user = request.user#associa o contato ao user
            contato.save() #salva o contato no banco de dados
            return redirect('agenda:contato_lista')
    else:
        form = ContatoForm()
    return render(request,
                  'agenda/contato_form.html',
                  {'form' : form,
                  'titulo_pagina': 'Adicionar Contato'})


def contato_teste(request):
    return HttpResponse('<h1>Teste</h1>')

@login_required()
def contato_detalhe(request, pk):
    contato = get_object_or_404(Contato, pk=pk, user=request.user)
    return render(request, 'agenda/contato_detalhe.html', {'contato' : contato})


@login_required()
def contato_editar(request, pk):
    contato = get_object_or_404(Contato, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('agenda:contato_detalhe', pk=contato.pk)
    else:
        form = ContatoForm(instance=contato)

    return render(request,
                  'agenda/contato_form.html',
                  {'form' : form, 'contato' : contato, 'titulo_pagina' : 'Editar'})


@login_required()
def contato_excluir(request, pk):
    contato = get_object_or_404(Contato, pk=pk, user=request.user)
    if request.method == 'POST':
        contato.delete()
        return redirect('agenda:contato_lista')

    return render(request,
                  'agenda/contato_confirma_exclusao.html',
                  {'contato' : contato})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redireciona para a página de login após o registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})