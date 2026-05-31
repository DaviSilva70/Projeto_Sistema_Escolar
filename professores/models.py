from django.db import models
from django.conf import settings
from core.models import TimeStampedModel


class Professor(TimeStampedModel):
    """Modelo de Professor"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil_professor')
    matricula = models.CharField(max_length=20, unique=True, verbose_name='Matrícula')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    formacao = models.CharField(max_length=100, verbose_name='Formação')
    especialidade = models.CharField(max_length=100, blank=True, verbose_name='Especialidade')
    data_admissao = models.DateField(verbose_name='Data de Admissão')
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salário')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['user__first_name']

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.especialidade}'
