from django.db import models
from core.models import TimeStampedModel


class Nota(TimeStampedModel):
    """Modelo de Nota"""
    TIPO_AVALIACAO_CHOICES = [
        ('prova', 'Prova'),
        ('trabalho', 'Trabalho'),
        ('atividade', 'Atividade'),
        ('participacao', 'Participação'),
    ]
    BIMESTRE_CHOICES = [
        (1, '1º Bimestre'),
        (2, '2º Bimestre'),
        (3, '3º Bimestre'),
        (4, '4º Bimestre'),
    ]

    aluno = models.ForeignKey('alunos.Aluno', on_delete=models.CASCADE, related_name='notas')
    disciplina = models.ForeignKey('disciplinas.Disciplina', on_delete=models.CASCADE, related_name='notas')
    turma = models.ForeignKey('turmas.Turma', on_delete=models.CASCADE, related_name='notas')
    bimestre = models.IntegerField(choices=BIMESTRE_CHOICES, verbose_name='Bimestre')
    tipo_avaliacao = models.CharField(max_length=20, choices=TIPO_AVALIACAO_CHOICES, verbose_name='Tipo de Avaliação')
    nota = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Nota')
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=1.0, verbose_name='Peso')
    data_avaliacao = models.DateField(verbose_name='Data da Avaliação')
    observacao = models.TextField(blank=True, verbose_name='Observação')

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['aluno', 'disciplina', 'bimestre']

    def __str__(self):
        return f'{self.aluno} - {self.disciplina} - {self.nota}'

    @property
    def nota_com_peso(self):
        return float(self.nota) * float(self.peso)
