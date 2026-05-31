from django.contrib import admin
from .models import Nota


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'disciplina', 'turma', 'bimestre', 'tipo_avaliacao', 'nota', 'peso', 'data_avaliacao']
    list_filter = ['bimestre', 'tipo_avaliacao', 'turma', 'disciplina']
    search_fields = ['aluno__user__first_name', 'aluno__user__last_name', 'aluno__ra']
    raw_id_fields = ['aluno', 'disciplina', 'turma']
