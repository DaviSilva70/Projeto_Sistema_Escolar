from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator
from .models import Comunicado
from .forms import ComunicadoForm
from core.utils.permissoes import perfil_requerido
from django.contrib.auth.decorators import login_required


@login_required
def lista_comunicados(request):
    if request.user.tipo == 'aluno':
        comunicados = Comunicado.objects.filter(para_todos=True)
    elif request.user.tipo == 'professor':
        comunicados = Comunicado.objects.all()
    else:
        comunicados = Comunicado.objects.all()
    paginator = Paginator(comunicados, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'comunicados/lista.html', {'page_obj': page_obj})


@perfil_requerido('admin', 'diretor', 'professor')
def cadastro_comunicado(request):
    if request.method == 'POST':
        form = ComunicadoForm(request.POST)
        if form.is_valid():
            try:
                comunicado = form.save(commit=False)
                comunicado.autor = request.user
                comunicado.save()
                messages.success(request, 'Comunicado criado com sucesso!')
                return redirect('lista_comunicados')
            except IntegrityError:
                messages.error(request, 'Erro de integridade: comunicado já existente ou dados duplicados.')
    else:
        form = ComunicadoForm()
    return render(request, 'comunicados/cadastro.html', {'form': form})


@login_required
def detalhe_comunicado(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    return render(request, 'comunicados/detalhe.html', {'comunicado': comunicado})


@login_required
def marcar_lido(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    if request.method == 'POST':
        comunicado.lido = True
        comunicado.save()
        messages.success(request, 'Comunicado marcado como lido!')
    return redirect('detalhe_comunicado', pk=pk)
