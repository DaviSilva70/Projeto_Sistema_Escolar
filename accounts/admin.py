from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'tipo', 'ativo']
    list_filter = ['tipo', 'ativo', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo', 'telefone', 'data_nascimento', 'foto', 'ativo')
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo', 'telefone', 'data_nascimento')
        }),
    )
