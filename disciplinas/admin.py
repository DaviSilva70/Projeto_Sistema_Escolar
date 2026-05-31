from django.contrib import admin
from .models import Disciplina, DisciplinaTurma


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'carga_horaria', 'obrigatoria', 'ativo']
    list_filter = ['obrigatoria', 'ativo']
    search_fields = ['nome']


@admin.register(DisciplinaTurma)
class DisciplinaTurmaAdmin(admin.ModelAdmin):
    list_display = ['disciplina', 'turma', 'professor']
    list_filter = ['turma', 'disciplina']
    raw_id_fields = ['disciplina', 'turma', 'professor']
