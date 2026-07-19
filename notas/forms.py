from django import forms
from django.core.exceptions import ValidationError

from .models import Nota

WIDGET_ATTRS = {'class': 'form-control-modern'}


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = [
            'aluno', 'disciplina', 'turma', 'bimestre',
            'tipo_avaliacao', 'nota', 'peso', 'data_avaliacao', 'observacao',
        ]
        widgets = {
            'aluno': forms.Select(attrs=WIDGET_ATTRS),
            'disciplina': forms.Select(attrs=WIDGET_ATTRS),
            'turma': forms.Select(attrs=WIDGET_ATTRS),
            'bimestre': forms.Select(attrs=WIDGET_ATTRS),
            'tipo_avaliacao': forms.Select(attrs=WIDGET_ATTRS),
            'nota': forms.NumberInput(attrs={**WIDGET_ATTRS, 'step': '0.01'}),
            'peso': forms.NumberInput(attrs={**WIDGET_ATTRS, 'step': '0.01'}),
            'data_avaliacao': forms.DateInput(attrs={**WIDGET_ATTRS, 'type': 'date'}),
            'observacao': forms.Textarea(attrs=WIDGET_ATTRS),
        }

    def clean_nota(self):
        nota = self.cleaned_data['nota']
        if nota < 0 or nota > 10:
            raise ValidationError('A nota deve estar entre 0 e 10.')
        return nota

    def clean_peso(self):
        peso = self.cleaned_data['peso']
        if peso <= 0:
            raise ValidationError('O peso deve ser maior que zero.')
        return peso

    def clean_bimestre(self):
        bimestre = self.cleaned_data['bimestre']
        if bimestre not in [1, 2, 3, 4]:
            raise ValidationError('O bimestre deve ser 1, 2, 3 ou 4.')
        return bimestre
