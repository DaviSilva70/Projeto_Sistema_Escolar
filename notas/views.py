from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Nota
from alunos.models import Aluno


@login_required
def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/lista.html', {'notas': notas})


@login_required
def lancamento_notas(request):
    if request.method == 'POST':
        try:
            Nota.objects.create(
                aluno_id=request.POST.get('aluno'),
                disciplina_id=request.POST.get('disciplina'),
                turma_id=request.POST.get('turma'),
                bimestre=request.POST.get('bimestre'),
                tipo_avaliacao=request.POST.get('tipo_avaliacao'),
                nota=request.POST.get('nota'),
                peso=request.POST.get('peso', 1.0),
                data_avaliacao=request.POST.get('data_avaliacao'),
                observacao=request.POST.get('observacao', ''),
            )
            messages.success(request, 'Nota lançada com sucesso!')
            return redirect('lista_notas')

        except Exception as e:
            messages.error(request, f'Erro ao lançar nota: {str(e)}')

    from alunos.models import Aluno
    from disciplinas.models import Disciplina
    from turmas.models import Turma

    return render(request, 'notas/lancamento.html', {
        'alunos': Aluno.objects.filter(ativo=True),
        'disciplinas': Disciplina.objects.filter(ativo=True),
        'turmas': Turma.objects.filter(ativo=True),
    })


@login_required
def boletim_aluno(request, aluno_pk):
    aluno = get_object_or_404(Aluno, pk=aluno_pk)
    notas = Nota.objects.filter(aluno=aluno)
    return render(request, 'notas/boletim.html', {'aluno': aluno, 'notas': notas})
