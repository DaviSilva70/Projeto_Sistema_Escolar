from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Turma


@login_required
def lista_turmas(request):
    turmas = Turma.objects.filter(ativo=True)
    return render(request, 'turmas/lista.html', {'turmas': turmas})


@login_required
def cadastro_turma(request):
    if request.method == 'POST':
        try:
            Turma.objects.create(
                nome=request.POST.get('nome'),
                nivel=request.POST.get('nivel'),
                serie=request.POST.get('serie'),
                turno=request.POST.get('turno'),
                ano_letivo=request.POST.get('ano_letivo'),
                capacidade=request.POST.get('capacidade', 40),
                sala=request.POST.get('sala', ''),
            )
            messages.success(request, 'Turma cadastrada com sucesso!')
            return redirect('lista_turmas')

        except Exception as e:
            messages.error(request, f'Erro ao cadastrar turma: {str(e)}')

    return render(request, 'turmas/cadastro.html')


@login_required
def detalhe_turma(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    return render(request, 'turmas/detalhe.html', {'turma': turma})


@login_required
def editar_turma(request, pk):
    turma = get_object_or_404(Turma, pk=pk)

    if request.method == 'POST':
        try:
            turma.nome = request.POST.get('nome', turma.nome)
            turma.nivel = request.POST.get('nivel', turma.nivel)
            turma.serie = request.POST.get('serie', turma.serie)
            turma.turno = request.POST.get('turno', turma.turno)
            turma.ano_letivo = request.POST.get('ano_letivo', turma.ano_letivo)
            turma.capacidade = request.POST.get('capacidade', turma.capacidade)
            turma.sala = request.POST.get('sala', turma.sala)
            turma.save()

            messages.success(request, 'Turma atualizada com sucesso!')
            return redirect('detalhe_turma', pk=pk)

        except Exception as e:
            messages.error(request, f'Erro ao atualizar turma: {str(e)}')

    return render(request, 'turmas/editar.html', {'turma': turma})
