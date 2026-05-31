from django.db import models
from django.conf import settings
from core.models import TimeStampedModel


class Frequencia(TimeStampedModel):
    """Modelo de Frequência"""
    PRESENCA_CHOICES = [
        ('P', 'Presente'),
        ('F', 'Ausente'),
        ('J', 'Justificado'),
        ('A', 'Atrasado'),
    ]

    aluno = models.ForeignKey('alunos.Aluno', on_delete=models.CASCADE, related_name='frequencias')
    turma = models.ForeignKey('turmas.Turma', on_delete=models.CASCADE, related_name='frequencias')
    data = models.DateField(verbose_name='Data')
    status = models.CharField(max_length=1, choices=PRESENCA_CHOICES, verbose_name='Status')
    justificativa = models.TextField(blank=True, verbose_name='Justificativa')
    registrado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='frequencias_registradas',
        verbose_name='Registrado por'
    )

    class Meta:
        verbose_name = 'Frequência'
        verbose_name_plural = 'Frequências'
        ordering = ['-data', 'aluno']
        unique_together = ['aluno', 'turma', 'data']

    def __str__(self):
        return f'{self.aluno} - {self.data} - {self.get_status_display()}'
