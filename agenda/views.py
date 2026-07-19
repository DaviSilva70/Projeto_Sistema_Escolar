from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator
from .models import Evento
from .forms import EventoForm
from core.utils.permissoes import perfil_requerido
from django.contrib.auth.decorators import login_required


@login_required
def lista_eventos(request):
    eventos = Evento.objects.all()
    paginator = Paginator(eventos, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'agenda/lista.html', {'page_obj': page_obj})


@perfil_requerido('admin', 'diretor', 'professor')
def cadastro_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            try:
                evento = form.save(commit=False)
                evento.responsavel = request.user
                evento.save()
                messages.success(request, 'Evento criado com sucesso!')
                return redirect('lista_eventos')
            except IntegrityError:
                messages.error(request, 'Erro de integridade: evento já existente ou dados duplicados.')
    else:
        form = EventoForm()
    return render(request, 'agenda/cadastro.html', {'form': form})


@perfil_requerido('admin', 'diretor', 'professor')
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Evento atualizado com sucesso!')
                return redirect('lista_eventos')
            except IntegrityError:
                messages.error(request, 'Erro de integridade: dados duplicados ou conflitantes.')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'agenda/editar.html', {'form': form, 'evento': evento})


@perfil_requerido('admin', 'diretor')
def excluir_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento excluído com sucesso!')
        return redirect('lista_eventos')
    return render(request, 'agenda/excluir.html', {'evento': evento})
