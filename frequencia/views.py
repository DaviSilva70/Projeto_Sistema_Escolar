from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Frequencia
from alunos.models import Aluno
from turmas.models import Turma, TurmaAluno


@login_required
def lista_frequencia(request):
    frequencias = Frequencia.objects.all()
    return render(request, 'frequencia/lista.html', {'frequencias': frequencias})


@login_required
def chamada(request):
    if request.method == 'POST':
        try:
            turma_id = request.POST.get('turma')
            data = request.POST.get('data')

            # Buscar alunos vinculados à turma via TurmaAluno
            alunos_vinculados = Aluno.objects.filter(
                turmaaluno__turma_id=turma_id, ativo=True
            )

            for aluno in alunos_vinculados:
                status = request.POST.get(f'status_{aluno.pk}', 'P')
                justificativa = request.POST.get(f'justificativa_{aluno.pk}', '')

                Frequencia.objects.create(
                    aluno=aluno,
                    turma_id=turma_id,
                    data=data,
                    status=status,
                    justificativa=justificativa,
                    registrado_por=request.user,
                )

            messages.success(request, 'Chamada registrada com sucesso!')
            return redirect('lista_frequencia')

        except Exception as e:
            messages.error(request, f'Erro ao registrar chamada: {str(e)}')

    turmas = Turma.objects.filter(ativo=True)
    alunos = []

    turma_id = request.GET.get('turma')
    if turma_id:
        # Buscar alunos vinculados à turma via TurmaAluno
        alunos = Aluno.objects.filter(
            turmaaluno__turma_id=turma_id, ativo=True
        ).select_related('user')

    return render(request, 'frequencia/chamada.html', {
        'turmas': turmas,
        'alunos': alunos,
        'turma_selecionada': turma_id,
    })


@login_required
def historico_frequencia(request, aluno_pk):
    aluno = get_object_or_404(Aluno, pk=aluno_pk)
    frequencias = Frequencia.objects.filter(aluno=aluno)
    return render(request, 'frequencia/historico.html', {'aluno': aluno, 'frequencias': frequencias})
