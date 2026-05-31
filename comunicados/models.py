from django.db import models
from django.conf import settings
from core.models import TimeStampedModel


class Comunicado(TimeStampedModel):
    """Modelo de Comunicado"""
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=200, verbose_name='Título')
    mensagem = models.TextField(verbose_name='Mensagem')
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='media', verbose_name='Prioridade')
    data_validade = models.DateField(null=True, blank=True, verbose_name='Data de Validade')
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comunicados_criados',
        verbose_name='Autor'
    )
    turmas = models.ManyToManyField('turmas.Turma', blank=True, related_name='comunicados')
    para_todos = models.BooleanField(default=False, verbose_name='Para Todos')
    lido = models.BooleanField(default=False, verbose_name='Lido')

    class Meta:
        verbose_name = 'Comunicado'
        verbose_name_plural = 'Comunicados'
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.titulo} - {self.get_prioridade_display()}'
