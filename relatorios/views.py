from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_relatorios(request):
    return render(request, 'relatorios/dashboard.html')


@login_required
def relatorio_desempenho(request):
    return render(request, 'relatorios/desempenho.html')


@login_required
def relatorio_frequencia(request):
    return render(request, 'relatorios/frequencia.html')
