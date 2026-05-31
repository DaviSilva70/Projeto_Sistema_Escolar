from django.db import models
from core.models import TimeStampedModel


class Disciplina(TimeStampedModel):
    """Modelo de Disciplina"""
    nome = models.CharField(max_length=100, verbose_name='Nome')
    carga_horaria = models.IntegerField(verbose_name='Carga Horária (horas)')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    obrigatoria = models.BooleanField(default=True, verbose_name='Obrigatória')
    ativo = models.BooleanField(default=True, verbose_name='Ativa')

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.carga_horaria}h)'


class DisciplinaTurma(models.Model):
    """Relação entre Disciplina, Turma e Professor"""
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='disciplinaturma')
    turma = models.ForeignKey('turmas.Turma', on_delete=models.CASCADE, related_name='disciplinaturma')
    professor = models.ForeignKey('professores.Professor', on_delete=models.CASCADE, related_name='disciplinaturma')

    class Meta:
        verbose_name = 'Disciplina da Turma'
        verbose_name_plural = 'Disciplinas das Turmas'
        unique_together = ['disciplina', 'turma']

    def __str__(self):
        return f'{self.disciplina} - {self.turma} - {self.professor}'
