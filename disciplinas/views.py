from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator
from .models import Disciplina
from .forms import DisciplinaForm
from core.utils.permissoes import perfil_requerido


@perfil_requerido('admin', 'diretor')
def lista_disciplinas(request):
    disciplinas_list = Disciplina.objects.filter(ativo=True)
    paginator = Paginator(disciplinas_list, 15)
    page_number = request.GET.get('page')
    disciplinas = paginator.get_page(page_number)
    return render(request, 'disciplinas/lista.html', {'disciplinas': disciplinas})


@perfil_requerido('admin', 'diretor')
def cadastro_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Disciplina cadastrada com sucesso!')
                return redirect('lista_disciplinas')
            except IntegrityError:
                messages.error(request, 'Erro: dados duplicados.')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = DisciplinaForm()
    return render(request, 'disciplinas/cadastro.html', {'form': form})


@perfil_requerido('admin', 'diretor')
def detalhe_disciplina(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    return render(request, 'disciplinas/detalhe.html', {'disciplina': disciplina})


@perfil_requerido('admin', 'diretor')
def editar_disciplina(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Disciplina atualizada com sucesso!')
                return redirect('detalhe_disciplina', pk=pk)
            except IntegrityError:
                messages.error(request, 'Erro: dados duplicados.')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'disciplinas/editar.html', {'form': form, 'disciplina': disciplina})


@perfil_requerido('admin', 'diretor')
def excluir_disciplina(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    if request.method == 'POST':
        try:
            disciplina.delete()
            messages.success(request, 'Disciplina excluída com sucesso!')
            return redirect('lista_disciplinas')
        except IntegrityError:
            messages.error(request, 'Erro ao excluir disciplina: dados dependentes.')
    return render(request, 'disciplinas/excluir.html', {'disciplina': disciplina})
