from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensalidade


@login_required
def lista_mensalidades(request):
    mensalidades = Mensalidade.objects.all()
    return render(request, 'financeiro/lista.html', {'mensalidades': mensalidades})


@login_required
def registrar_pagamento(request, pk):
    mensalidade = get_object_or_404(Mensalidade, pk=pk)
    if request.method == 'POST':
        from datetime import date
        mensalidade.status = 'pago'
        mensalidade.data_pagamento = date.today()
        mensalidade.save()
        messages.success(request, 'Pagamento registrado com sucesso!')
        return redirect('lista_mensalidades')
    return render(request, 'financeiro/pagamento.html', {'mensalidade': mensalidade})
