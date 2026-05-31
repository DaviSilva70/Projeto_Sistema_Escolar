from django.db import models
from core.models import TimeStampedModel


class Mensalidade(TimeStampedModel):
    """Modelo de Mensalidade"""
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('atrasado', 'Atrasado'),
        ('isento', 'Isento'),
    ]

    aluno = models.ForeignKey('alunos.Aluno', on_delete=models.CASCADE, related_name='mensalidades')
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    data_vencimento = models.DateField(verbose_name='Data de Vencimento')
    data_pagamento = models.DateField(null=True, blank=True, verbose_name='Data de Pagamento')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', verbose_name='Status')
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Desconto')
    observacao = models.TextField(blank=True, verbose_name='Observação')

    class Meta:
        verbose_name = 'Mensalidade'
        verbose_name_plural = 'Mensalidades'
        ordering = ['data_vencimento']

    def __str__(self):
        return f'{self.aluno} - R$ {self.valor} - {self.get_status_display()}'

    @property
    def valor_final(self):
        return float(self.valor) - float(self.desconto)
