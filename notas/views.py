from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator
from .models import Nota
from .forms import NotaForm
from alunos.models import Aluno
from core.utils.permissoes import perfil_requerido


@perfil_requerido('admin', 'diretor', 'professor')
def lista_notas(request):
    notas_list = Nota.objects.all()
    paginator = Paginator(notas_list, 15)
    page_number = request.GET.get('page')
    notas = paginator.get_page(page_number)
    return render(request, 'notas/lista.html', {'notas': notas})


@perfil_requerido('admin', 'diretor', 'professor')
def lancamento_notas(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Nota lançada com sucesso!')
                return redirect('lista_notas')
            except IntegrityError:
                messages.error(
                    request,
                    'Já existe uma nota para este aluno, disciplina, bimestre e tipo de avaliação.',
                )
    else:
        form = NotaForm()
    return render(request, 'notas/lancamento.html', {'form': form})


@perfil_requerido('admin', 'diretor', 'professor')
def boletim_aluno(request, aluno_pk):
    aluno = get_object_or_404(Aluno, pk=aluno_pk)
    notas = Nota.objects.filter(aluno=aluno)
    return render(request, 'notas/boletim.html', {'aluno': aluno, 'notas': notas})
