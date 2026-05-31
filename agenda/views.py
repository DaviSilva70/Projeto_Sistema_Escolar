from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Evento


@login_required
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'agenda/lista.html', {'eventos': eventos})


@login_required
def cadastro_evento(request):
    if request.method == 'POST':
        try:
            Evento.objects.create(
                titulo=request.POST.get('titulo'),
                descricao=request.POST.get('descricao'),
                data_inicio=request.POST.get('data_inicio'),
                data_fim=request.POST.get('data_fim'),
                local=request.POST.get('local', ''),
                responsavel=request.user,
                cor=request.POST.get('cor', '#4f46e5'),
            )
            messages.success(request, 'Evento criado com sucesso!')
            return redirect('lista_eventos')

        except Exception as e:
            messages.error(request, f'Erro ao criar evento: {str(e)}')

    return render(request, 'agenda/cadastro.html')
