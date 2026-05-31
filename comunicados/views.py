from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Comunicado


@login_required
def lista_comunicados(request):
    comunicados = Comunicado.objects.all()
    return render(request, 'comunicados/lista.html', {'comunicados': comunicados})


@login_required
def cadastro_comunicado(request):
    if request.method == 'POST':
        try:
            comunicado = Comunicado.objects.create(
                titulo=request.POST.get('titulo'),
                mensagem=request.POST.get('mensagem'),
                prioridade=request.POST.get('prioridade', 'media'),
                data_validade=request.POST.get('data_validade') or None,
                autor=request.user,
                para_todos=request.POST.get('para_todos') == 'on',
            )
            messages.success(request, 'Comunicado criado com sucesso!')
            return redirect('lista_comunicados')

        except Exception as e:
            messages.error(request, f'Erro ao criar comunicado: {str(e)}')

    return render(request, 'comunicados/cadastro.html')


@login_required
def detalhe_comunicado(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    return render(request, 'comunicados/detalhe.html', {'comunicado': comunicado})
