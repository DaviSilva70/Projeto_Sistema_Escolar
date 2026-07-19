from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'disciplina', 'autor', 'ativo', 'criado_em']
    list_filter = ['categoria', 'ativo', 'disciplina']
    search_fields = ['titulo', 'descricao']
    list_editable = ['ativo']
