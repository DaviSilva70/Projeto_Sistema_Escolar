from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator
from .models import Frequencia
from .forms import FrequenciaForm
from alunos.models import Aluno
from turmas.models import Turma, TurmaAluno
from core.utils.permissoes import perfil_requerido


@perfil_requerido('admin', 'diretor', 'professor')
def lista_frequencia(request):
    frequencias_list = Frequencia.objects.all()
    paginator = Paginator(frequencias_list, 15)
    page_number = request.GET.get('page')
    frequencias = paginator.get_page(page_number)
    return render(request, 'frequencia/lista.html', {'frequencias': frequencias})


@perfil_requerido('admin', 'diretor', 'professor')
def chamada(request):
    if request.method == 'POST':
        turma_id = request.POST.get('turma')
        data = request.POST.get('data')

        alunos_vinculados = Aluno.objects.filter(
            turmaaluno__turma_id=turma_id, ativo=True
        )

        erros = []
        for aluno in alunos_vinculados:
            status = request.POST.get(f'status_{aluno.pk}', 'P')
            justificativa = request.POST.get(f'justificativa_{aluno.pk}', '')

            try:
                Frequencia.objects.create(
                    aluno=aluno,
                    turma_id=turma_id,
                    data=data,
                    status=status,
                    justificativa=justificativa,
                    registrado_por=request.user,
                )
            except IntegrityError:
                erros.append(aluno.user.get_full_name() or str(aluno))

        if erros:
            nomes = ', '.join(erros)
            messages.warning(
                request,
                f'Registros ignorados (já existentes): {nomes}',
            )
        if len(erros) < len(alunos_vinculados):
            messages.success(request, 'Chamada registrada com sucesso!')
        return redirect('lista_frequencia')

    turmas = Turma.objects.filter(ativo=True)
    alunos = []
    turma_id = request.GET.get('turma')
    if turma_id:
        alunos = Aluno.objects.filter(
            turmaaluno__turma_id=turma_id, ativo=True
        ).select_related('user')

    return render(request, 'frequencia/chamada.html', {
        'turmas': turmas,
        'alunos': alunos,
        'turma_selecionada': turma_id,
    })


@perfil_requerido('admin', 'diretor', 'professor')
def historico_frequencia(request, aluno_pk):
    aluno = get_object_or_404(Aluno, pk=aluno_pk)
    frequencias_list = Frequencia.objects.filter(aluno=aluno)
    paginator = Paginator(frequencias_list, 15)
    page_number = request.GET.get('page')
    frequencias = paginator.get_page(page_number)
    return render(request, 'frequencia/historico.html', {
        'aluno': aluno,
        'frequencias': frequencias,
    })
