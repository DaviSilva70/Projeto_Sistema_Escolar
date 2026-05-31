from django.db import models


class TimeStampedModel(models.Model):
    """Modelo abstrato com timestamps"""
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        abstract = True
        ordering = ['-criado_em']


class AtivoManager(models.Manager):
    """Manager para filtrar apenas registros ativos"""
    def get_queryset(self):
        return super().get_queryset().filter(ativo=True)
