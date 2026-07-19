from django import forms
from django.core.exceptions import ValidationError

from .models import Turma

WIDGET_ATTRS = {'class': 'form-control-modern'}


class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'nivel', 'serie', 'turno', 'ano_letivo', 'capacidade', 'sala']
        widgets = {
            'nome': forms.TextInput(attrs=WIDGET_ATTRS),
            'nivel': forms.Select(attrs=WIDGET_ATTRS),
            'serie': forms.NumberInput(attrs=WIDGET_ATTRS),
            'turno': forms.Select(attrs=WIDGET_ATTRS),
            'ano_letivo': forms.NumberInput(attrs=WIDGET_ATTRS),
            'capacidade': forms.NumberInput(attrs=WIDGET_ATTRS),
            'sala': forms.TextInput(attrs=WIDGET_ATTRS),
        }

    def clean_serie(self):
        serie = self.cleaned_data['serie']
        if not (1 <= serie <= 9):
            raise ValidationError('A série deve ser um número entre 1 e 9.')
        return serie

    def clean_capacidade(self):
        capacidade = self.cleaned_data['capacidade']
        if capacidade <= 0:
            raise ValidationError('A capacidade deve ser maior que zero.')
        return capacidade

    def clean_ano_letivo(self):
        ano = self.cleaned_data['ano_letivo']
        if ano < 2020:
            raise ValidationError('O ano letivo deve ser maior ou igual a 2020.')
        return ano
