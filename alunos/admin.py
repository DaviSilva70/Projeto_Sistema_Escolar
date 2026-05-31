from django.contrib import admin
from .models import Responsavel, Aluno


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'tipo', 'cpf', 'telefone', 'endereco']
    list_filter = ['tipo']
    search_fields = ['nome_completo', 'cpf', 'telefone']


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['ra', 'user', 'cpf', 'data_nascimento', 'responsavel', 'ativo']
    list_filter = ['ativo', 'data_nascimento']
    search_fields = ['ra', 'cpf', 'user__first_name', 'user__last_name']
    raw_id_fields = ['user', 'responsavel']
