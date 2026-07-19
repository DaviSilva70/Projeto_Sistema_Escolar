from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator
from .models import Turma
from .forms import TurmaForm
from core.utils.permissoes import perfil_requerido


@perfil_requerido('admin', 'diretor')
def lista_turmas(request):
    turmas_list = Turma.objects.filter(ativo=True)
    paginator = Paginator(turmas_list, 15)
    page_number = request.GET.get('page')
    turmas = paginator.get_page(page_number)
    return render(request, 'turmas/lista.html', {'turmas': turmas})


@perfil_requerido('admin', 'diretor')
def cadastro_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Turma cadastrada com sucesso!')
                return redirect('lista_turmas')
            except IntegrityError:
                messages.error(request, 'Erro: dados duplicados.')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = TurmaForm()
    return render(request, 'turmas/cadastro.html', {'form': form})


@perfil_requerido('admin', 'diretor')
def detalhe_turma(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    return render(request, 'turmas/detalhe.html', {'turma': turma})


@perfil_requerido('admin', 'diretor')
def editar_turma(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Turma atualizada com sucesso!')
                return redirect('detalhe_turma', pk=pk)
            except IntegrityError:
                messages.error(request, 'Erro: dados duplicados.')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'turmas/editar.html', {'form': form, 'turma': turma})
