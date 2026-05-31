from django.contrib import admin
from .models import Evento


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_inicio', 'data_fim', 'local', 'responsavel', 'cor']
    list_filter = ['data_inicio', 'responsavel']
    search_fields = ['titulo', 'descricao', 'local']
    raw_id_fields = ['responsavel']
    filter_horizontal = ['turmas']
