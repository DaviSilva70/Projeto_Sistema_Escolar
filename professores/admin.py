from django.contrib import admin
from .models import Professor


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'user', 'cpf', 'formacao', 'especialidade', 'ativo']
    list_filter = ['ativo', 'formacao']
    search_fields = ['matricula', 'cpf', 'user__first_name', 'user__last_name']
    raw_id_fields = ['user']
