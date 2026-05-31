from django.db import models
from core.models import TimeStampedModel


class Turma(TimeStampedModel):
    """Modelo de Turma"""
    NIVEL_CHOICES = [
        ('fundamental1', 'Fundamental I'),
        ('fundamental2', 'Fundamental II'),
        ('medio', 'Médio'),
    ]
    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
    ]

    nome = models.CharField(max_length=50, verbose_name='Nome')
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, verbose_name='Nível')
    serie = models.IntegerField(verbose_name='Série')
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES, verbose_name='Turno')
    ano_letivo = models.IntegerField(verbose_name='Ano Letivo')
    capacidade = models.IntegerField(default=40, verbose_name='Capacidade')
    sala = models.CharField(max_length=20, blank=True, verbose_name='Sala')
    ativo = models.BooleanField(default=True, verbose_name='Ativa')

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['ano_letivo', 'nivel', 'serie', 'turno']

    def __str__(self):
        return f'{self.nome} - {self.get_nivel_display()} - {self.ano_letivo}'

    @property
    def vagas_disponiveis(self):
        from alunos.models import Aluno
        matriculados = Aluno.objects.filter(turmaaluno__turma=self).count()
        return self.capacidade - matriculados


class TurmaAluno(models.Model):
    """Relação entre Turma e Aluno"""
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='turmaaluno')
    aluno = models.ForeignKey('alunos.Aluno', on_delete=models.CASCADE, related_name='turmaaluno')
    data_matricula = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
        unique_together = ['turma', 'aluno']

    def __str__(self):
        return f'{self.aluno} - {self.turma}'
