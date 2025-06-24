#agenda/views.py

from django.shortcuts import render, redirect
from .models import Contato
from .forms import ContatoForm

#Biblioteca para escrever codigo html diretamente da view
from django.http import HttpResponse

def contato_lista(request):
    contatos = Contato.objects.all().order_by('nome')
    return render(request,
                  'agenda/contato_lista.html',
                  {'contatos' : contatos})


def contato_criar(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:contato_lista')
    else:
        form = ContatoForm()
        return render(request,
                      'agenda/contato_form.html',
                      {'form' : form,
                      'titulo_pagina': 'Adicionar Contato'})