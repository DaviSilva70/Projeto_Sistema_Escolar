from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Disciplina


@login_required
def lista_disciplinas(request):
    disciplinas = Disciplina.objects.filter(ativo=True)
    return render(request, 'disciplinas/lista.html', {'disciplinas': disciplinas})


@login_required
def cadastro_disciplina(request):
    if request.method == 'POST':
        try:
            Disciplina.objects.create(
                nome=request.POST.get('nome'),
                carga_horaria=request.POST.get('carga_horaria'),
                descricao=request.POST.get('descricao', ''),
                obrigatoria=request.POST.get('obrigatoria', 'True') == 'True',
            )
            messages.success(request, 'Disciplina cadastrada com sucesso!')
            return redirect('lista_disciplinas')

        except Exception as e:
            messages.error(request, f'Erro ao cadastrar disciplina: {str(e)}')

    return render(request, 'disciplinas/cadastro.html')


@login_required
def detalhe_disciplina(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    return render(request, 'disciplinas/detalhe.html', {'disciplina': disciplina})
