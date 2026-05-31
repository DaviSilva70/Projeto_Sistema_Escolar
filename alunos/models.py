from django.db import models
from django.conf import settings
from core.models import TimeStampedModel


class Responsavel(TimeStampedModel):
    """Modelo de Responsável pelo Aluno"""
    TIPO_CHOICES = [
        ('mae', 'Mãe'),
        ('pai', 'Pai'),
        ('avo_materno', 'Avô Materno'),
        ('ava_materna', 'Avó Materna'),
        ('avo_paterno', 'Avô Paterno'),
        ('ava_paterna', 'Avó Paterna'),
        ('tio', 'Tio(a)'),
        ('irmao', 'Irmão(ã)'),
        ('tutor', 'Tutor(a)'),
        ('outro', 'Outro'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name='Parentesco')
    nome_completo = models.CharField(max_length=200, verbose_name='Nome Completo')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    email = models.CharField(max_length=200, blank=True, verbose_name='E-mail')
    endereco = models.TextField(verbose_name='Endereço Completo')
    profissao = models.CharField(max_length=100, blank=True, verbose_name='Profissão')
    local_trabalho = models.CharField(max_length=100, blank=True, verbose_name='Local de Trabalho')
    observacao = models.TextField(blank=True, verbose_name='Observação')

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'
        ordering = ['nome_completo']

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.nome_completo}'


class Aluno(TimeStampedModel):
    """Modelo de Aluno"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil_aluno')
    ra = models.CharField(max_length=20, unique=True, verbose_name='RA (Registro do Aluno)')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    rg = models.CharField(max_length=20, blank=True, verbose_name='RG')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    endereco = models.TextField(blank=True, verbose_name='Endereço')
    responsavel = models.ForeignKey(
        Responsavel,
        on_delete=models.PROTECT,
        related_name='alunos',
        verbose_name='Responsável'
    )
    foto = models.ImageField(upload_to='alunos/', null=True, blank=True, verbose_name='Foto')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['user__first_name']

    def __str__(self):
        return f'{self.user.get_full_name()} - RA: {self.ra}'

    @property
    def idade(self):
        from datetime import date
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - (
            (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )
