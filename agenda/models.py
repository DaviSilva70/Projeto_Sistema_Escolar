from django.db import models
from django.conf import settings
from core.models import TimeStampedModel


class Evento(TimeStampedModel):
    """Modelo de Evento"""
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    data_inicio = models.DateTimeField(verbose_name='Data/Hora Início')
    data_fim = models.DateTimeField(verbose_name='Data/Hora Fim')
    local = models.CharField(max_length=200, blank=True, verbose_name='Local')
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='eventos',
        verbose_name='Responsável'
    )
    turmas = models.ManyToManyField('turmas.Turma', blank=True, related_name='eventos')
    cor = models.CharField(max_length=7, default='#007bff', verbose_name='Cor')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['data_inicio']

    def __str__(self):
        return f'{self.titulo} - {self.data_inicio}'
