from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db import IntegrityError
from .models import Video
from .forms import VideoForm
from core.utils.permissoes import perfil_requerido


@login_required
def lista_videos(request):
    """Lista todos os vídeos ativos — todos os perfis logados"""
    videos_list = Video.objects.filter(ativo=True)
    paginator = Paginator(videos_list, 12)
    page = request.GET.get('page')
    videos = paginator.get_page(page)
    return render(request, 'videos/lista.html', {'videos': videos})


@login_required
def detalhe_video(request, pk):
    """Detalhes de um vídeo — todos os perfis logados"""
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'videos/detalhe.html', {'video': video})


@perfil_requerido('admin', 'diretor', 'professor')
def cadastro_video(request):
    """Cadastrar vídeo — apenas admin, diretor, professor"""
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            try:
                video = form.save(commit=False)
                video.autor = request.user
                video.save()
                form.save_m2m()
                messages.success(request, 'Vídeo cadastrado com sucesso!')
                return redirect('lista_videos')
            except IntegrityError:
                messages.error(request, 'Erro ao cadastrar vídeo. Dados duplicados.')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = VideoForm()
    return render(request, 'videos/cadastro.html', {'form': form})


@perfil_requerido('admin', 'diretor', 'professor')
def editar_video(request, pk):
    """Editar vídeo — apenas admin, diretor, professor (autor ou admin)"""
    video = get_object_or_404(Video, pk=pk)
    if request.user.tipo not in ('admin', 'diretor') and video.autor != request.user:
        messages.error(request, 'Você não tem permissão para editar este vídeo.')
        return redirect('lista_videos')

    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Vídeo atualizado com sucesso!')
                return redirect('detalhe_video', pk=pk)
            except IntegrityError:
                messages.error(request, 'Erro ao atualizar vídeo.')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = VideoForm(instance=video)
    return render(request, 'videos/editar.html', {'form': form, 'video': video})


@perfil_requerido('admin', 'diretor')
def excluir_video(request, pk):
    """Excluir vídeo — apenas admin e diretor"""
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        messages.success(request, 'Vídeo excluído com sucesso!')
        return redirect('lista_videos')
    return render(request, 'videos/excluir.html', {'video': video})
