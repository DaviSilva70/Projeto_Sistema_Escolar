from django.contrib import admin
from .models import Comunicado


@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'prioridade', 'autor', 'para_todos', 'data_validade', 'lido']
    list_filter = ['prioridade', 'para_todos', 'lido']
    search_fields = ['titulo', 'mensagem']
    raw_id_fields = ['autor']
    filter_horizontal = ['turmas']
