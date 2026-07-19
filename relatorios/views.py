from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Avg, Count, Q
from core.utils.permissoes import perfil_requerido


@login_required
def dashboard_relatorios(request):
    """Dashboard de relatórios com estatísticas gerais"""
    from alunos.models import Aluno
    from professores.models import Professor
    from turmas.models import Turma
    from disciplinas.models import Disciplina
    from notas.models import Nota
    from frequencia.models import Frequencia
    from financeiro.models import Mensalidade

    context = {
        'total_alunos': Aluno.objects.filter(ativo=True).count(),
        'total_professores': Professor.objects.filter(ativo=True).count(),
        'total_turmas': Turma.objects.filter(ativo=True).count(),
        'total_disciplinas': Disciplina.objects.filter(ativo=True).count(),
        'total_notas': Nota.objects.count(),
        'media_geral': Nota.objects.aggregate(media=Avg('nota'))['media'] or 0,
        'total_frequencias': Frequencia.objects.count(),
        'presencas': Frequencia.objects.filter(status='P').count(),
        'mensalidades_pendentes': Mensalidade.objects.filter(status='pendente').count(),
        'mensalidades_atrasadas': Mensalidade.objects.filter(status='atrasado').count(),
    }
    return render(request, 'relatorios/dashboard.html', context)


@perfil_requerido('admin', 'diretor')
def relatorio_desempenho(request):
    """Relatório de desempenho acadêmico por turma e disciplina"""
    from notas.models import Nota
    from turmas.models import Turma
    from disciplinas.models import Disciplina

    turma_id = request.GET.get('turma')
    disciplina_id = request.GET.get('disciplina')

    notas = Nota.objects.select_related('aluno__user', 'disciplina', 'turma').all()

    if turma_id:
        notas = notas.filter(turma_id=turma_id)
    if disciplina_id:
        notas = notas.filter(disciplina_id=disciplina_id)

    # Média por disciplina
    media_por_disciplina = (
        notas.values('disciplina__nome')
        .annotate(media=Avg('nota'), total=Count('id'))
        .order_by('disciplina__nome')
    )

    # Média por aluno
    media_por_aluno = (
        notas.values('aluno__user__first_name', 'aluno__user__last_name', 'aluno__ra')
        .annotate(media=Avg('nota'), total=Count('id'))
        .order_by('-media')
    )

    # Estatísticas gerais
    total_notas = notas.count()
    media_geral = notas.aggregate(media=Avg('nota'))['media'] or 0
    aprovados = notas.filter(nota__gte=7).count()
    reprovados = notas.filter(nota__lt=5).count()
    recuperacao = notas.filter(nota__gte=5, nota__lt=7).count()

    context = {
        'notas': notas[:100],
        'media_por_disciplina': media_por_disciplina,
        'media_por_aluno': media_por_aluno[:20],
        'turmas': Turma.objects.filter(ativo=True),
        'disciplinas': Disciplina.objects.filter(ativo=True),
        'turma_selecionada': turma_id,
        'disciplina_selecionada': disciplina_id,
        'total_notas': total_notas,
        'media_geral': round(media_geral, 2),
        'aprovados': aprovados,
        'reprovados': reprovados,
        'recuperacao': recuperacao,
    }
    return render(request, 'relatorios/desempenho.html', context)


@perfil_requerido('admin', 'diretor')
def relatorio_frequencia(request):
    """Relatório de frequência por turma"""
    from frequencia.models import Frequencia
    from turmas.models import Turma

    turma_id = request.GET.get('turma')

    frequencias = Frequencia.objects.select_related('aluno__user', 'turma').all()

    if turma_id:
        frequencias = frequencias.filter(turma_id=turma_id)

    # Estatísticas de frequência
    total = frequencias.count()
    presentes = frequencias.filter(status='P').count()
    ausentes = frequencias.filter(status='F').count()
    justificados = frequencias.filter(status='J').count()
    atrasados = frequencias.filter(status='A').count()
    percentual_presenca = (presentes / total * 100) if total > 0 else 0

    # Frequência por turma
    frequencia_por_turma = (
        frequencias.values('turma__nome')
        .annotate(
            total=Count('id'),
            presentes=Count('id', filter=Q(status='P')),
        )
        .order_by('turma__nome')
    )

    context = {
        'frequencias': frequencias[:100],
        'turmas': Turma.objects.filter(ativo=True),
        'turma_selecionada': turma_id,
        'total': total,
        'presentes': presentes,
        'ausentes': ausentes,
        'justificados': justificados,
        'atrasados': atrasados,
        'percentual_presenca': round(percentual_presenca, 1),
        'frequencia_por_turma': frequencia_por_turma,
    }
    return render(request, 'relatorios/frequencia.html', context)


@perfil_requerido('admin', 'diretor')
def relatorio_desempenho_pdf(request):
    """Gerar PDF do relatório de desempenho"""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from notas.models import Nota

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_desempenho.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Título
    elements.append(Paragraph("Relatório de Desempenho Acadêmico", styles['Title']))
    elements.append(Spacer(1, 20))

    # Dados
    notas = Nota.objects.select_related('aluno__user', 'disciplina').all()
    media_geral = notas.aggregate(media=Avg('nota'))['media'] or 0

    elements.append(Paragraph(f"Média Geral: {media_geral:.2f}", styles['Heading2']))
    elements.append(Paragraph(f"Total de Notas: {notas.count()}", styles['Normal']))
    elements.append(Spacer(1, 20))

    # Tabela por disciplina
    from django.db.models import Avg, Count
    media_por_disciplina = (
        notas.values('disciplina__nome')
        .annotate(media=Avg('nota'), total=Count('id'))
        .order_by('disciplina__nome')
    )

    data = [['Disciplina', 'Média', 'Total de Notas']]
    for item in media_por_disciplina:
        data.append([
            item['disciplina__nome'],
            f"{item['media']:.2f}",
            str(item['total'])
        ])

    if len(data) > 1:
        table = Table(data, colWidths=[200, 100, 100])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4f46e5')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f8fafc')),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ]))
        elements.append(table)

    doc.build(elements)
    return response


@perfil_requerido('admin', 'diretor')
def relatorio_frequencia_pdf(request):
    """Gerar PDF do relatório de frequência"""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from frequencia.models import Frequencia

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_frequencia.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Relatório de Frequência", styles['Title']))
    elements.append(Spacer(1, 20))

    total = Frequencia.objects.count()
    presentes = Frequencia.objects.filter(status='P').count()
    percentual = (presentes / total * 100) if total > 0 else 0

    elements.append(Paragraph(f"Total de Registros: {total}", styles['Normal']))
    elements.append(Paragraph(f"Presenças: {presentes} ({percentual:.1f}%)", styles['Normal']))
    elements.append(Paragraph(f"Ausências: {Frequencia.objects.filter(status='F').count()}", styles['Normal']))
    elements.append(Paragraph(f"Justificados: {Frequencia.objects.filter(status='J').count()}", styles['Normal']))
    elements.append(Spacer(1, 20))

    # Tabela por turma
    from django.db.models import Count, Q
    freq_turma = (
        Frequencia.objects.values('turma__nome')
        .annotate(
            total=Count('id'),
            presentes=Count('id', filter=Q(status='P')),
        )
        .order_by('turma__nome')
    )

    data = [['Turma', 'Total', 'Presenças', '% Presença']]
    for item in freq_turma:
        pct = (item['presentes'] / item['total'] * 100) if item['total'] > 0 else 0
        data.append([
            item['turma__nome'],
            str(item['total']),
            str(item['presentes']),
            f"{pct:.1f}%"
        ])

    if len(data) > 1:
        table = Table(data, colWidths=[150, 80, 80, 100])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#10b981')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f8fafc')),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ]))
        elements.append(table)

    doc.build(elements)
    return response
