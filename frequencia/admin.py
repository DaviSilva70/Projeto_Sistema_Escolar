from django.contrib import admin
from .models import Frequencia


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'turma', 'data', 'status', 'registrado_por']
    list_filter = ['status', 'turma', 'data']
    search_fields = ['aluno__user__first_name', 'aluno__user__last_name', 'aluno__ra']
    raw_id_fields = ['aluno', 'turma', 'registrado_por']
