from django.contrib import admin
from .models import Mensalidade


@admin.register(Mensalidade)
class MensalidadeAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'valor', 'data_vencimento', 'data_pagamento', 'status', 'desconto']
    list_filter = ['status', 'data_vencimento']
    search_fields = ['aluno__user__first_name', 'aluno__user__last_name', 'aluno__ra']
    raw_id_fields = ['aluno']
