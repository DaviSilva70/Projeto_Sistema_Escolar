from django.db import models
from django.conf import settings
from core.models import TimeStampedModel


class Video(TimeStampedModel):
    """Modelo de Video Educacional"""
    CATEGORIA_CHOICES = [
        ('aula', 'Aula'),
        ('tutorial', 'Tutorial'),
        ('palestra', 'Palestra'),
        ('documentario', 'Documentário'),
        ('animacao', 'Animação Educacional'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    url = models.URLField(verbose_name='URL do Vídeo (YouTube/Vimeo)')
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='aula', verbose_name='Categoria')
    disciplina = models.ForeignKey(
        'disciplinas.Disciplina',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='videos',
        verbose_name='Disciplina'
    )
    turmas = models.ManyToManyField('turmas.Turma', blank=True, related_name='videos', verbose_name='Turmas')
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='videos_criados',
        verbose_name='Autor'
    )
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    ordem = models.IntegerField(default=0, verbose_name='Ordem de Exibição')

    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'
        ordering = ['ordem', '-criado_em']

    def __str__(self):
        return f'{self.titulo} - {self.get_categoria_display()}'

    @property
    def youtube_embed_url(self):
        """Converte URL do YouTube para URL de embed"""
        url = self.url
        if 'youtube.com/watch' in url:
            video_id = url.split('v=')[1].split('&')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        elif 'youtu.be/' in url:
            video_id = url.split('youtu.be/')[1].split('?')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        return url
