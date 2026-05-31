from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Modelo de Usuário customizado"""
    TIPO_CHOICES = [
        ('admin', 'Administrador'),
        ('diretor', 'Diretor'),
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
        ('responsavel', 'Responsável'),
        ('funcionario', 'Funcionário'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='aluno')
    telefone = models.CharField(max_length=20, blank=True, verbose_name='Telefone')
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    foto = models.ImageField(upload_to='usuarios/', null=True, blank=True, verbose_name='Foto')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['first_name']

    def __str__(self):
        return f'{self.get_full_name()} ({self.get_tipo_display()})'

    @property
    def is_admin(self):
        return self.tipo == 'admin'

    @property
    def is_diretor(self):
        return self.tipo == 'diretor'

    @property
    def is_professor(self):
        return self.tipo == 'professor'

    @property
    def is_aluno(self):
        return self.tipo == 'aluno'

    @property
    def is_responsavel(self):
        return self.tipo == 'responsavel'
