from django.contrib import admin
from .models import Turma, TurmaAluno


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nivel', 'serie', 'turno', 'ano_letivo', 'capacidade', 'sala']
    list_filter = ['nivel', 'turno', 'ano_letivo']
    search_fields = ['nome', 'sala']


@admin.register(TurmaAluno)
class TurmaAlunoAdmin(admin.ModelAdmin):
    list_display = ['turma', 'aluno', 'data_matricula', 'ativo']
    list_filter = ['ativo', 'turma']
    raw_id_fields = ['turma', 'aluno']
