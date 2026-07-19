from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator
from datetime import date
from .models import Mensalidade
from .forms import MensalidadeForm
from core.utils.permissoes import perfil_requerido


@perfil_requerido('admin', 'diretor')
def lista_mensalidades(request):
    mensalidades = Mensalidade.objects.all()
    paginator = Paginator(mensalidades, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'financeiro/lista.html', {'page_obj': page_obj})


@perfil_requerido('admin', 'diretor')
def registrar_pagamento(request, pk):
    mensalidade = get_object_or_404(Mensalidade, pk=pk)
    if request.method == 'POST':
        mensalidade.status = 'pago'
        mensalidade.data_pagamento = date.today()
        mensalidade.save()
        messages.success(request, 'Pagamento registrado com sucesso!')
        return redirect('lista_mensalidades')
    return render(request, 'financeiro/pagamento.html', {'mensalidade': mensalidade})


@perfil_requerido('admin', 'diretor')
def cadastro_mensalidade(request):
    if request.method == 'POST':
        form = MensalidadeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Mensalidade cadastrada com sucesso!')
                return redirect('lista_mensalidades')
            except IntegrityError:
                messages.error(request, 'Erro de integridade: mensalidade já existente ou dados duplicados.')
    else:
        form = MensalidadeForm()
    return render(request, 'financeiro/cadastro.html', {'form': form})


@perfil_requerido('admin', 'diretor')
def editar_mensalidade(request, pk):
    mensalidade = get_object_or_404(Mensalidade, pk=pk)
    if request.method == 'POST':
        form = MensalidadeForm(request.POST, instance=mensalidade)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Mensalidade atualizada com sucesso!')
                return redirect('lista_mensalidades')
            except IntegrityError:
                messages.error(request, 'Erro de integridade: dados duplicados ou conflitantes.')
    else:
        form = MensalidadeForm(instance=mensalidade)
    return render(request, 'financeiro/editar.html', {'form': form, 'mensalidade': mensalidade})
