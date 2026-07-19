from django import forms
from django.core.exceptions import ValidationError

from .models import Mensalidade

WIDGET_ATTRS = {'class': 'form-control-modern'}


class MensalidadeForm(forms.ModelForm):
    class Meta:
        model = Mensalidade
        fields = ['aluno', 'valor', 'data_vencimento', 'status', 'desconto', 'observacao']
        exclude = ['data_pagamento']
        widgets = {
            'aluno': forms.Select(attrs=WIDGET_ATTRS),
            'valor': forms.NumberInput(attrs={**WIDGET_ATTRS, 'step': '0.01'}),
            'data_vencimento': forms.DateInput(attrs={**WIDGET_ATTRS, 'type': 'date'}),
            'status': forms.Select(attrs=WIDGET_ATTRS),
            'desconto': forms.NumberInput(attrs={**WIDGET_ATTRS, 'step': '0.01'}),
            'observacao': forms.Textarea(attrs=WIDGET_ATTRS),
        }

    def clean_valor(self):
        valor = self.cleaned_data['valor']
        if valor <= 0:
            raise ValidationError('O valor deve ser maior que zero.')
        return valor

    def clean_desconto(self):
        desconto = self.cleaned_data['desconto']
        if desconto < 0:
            raise ValidationError('O desconto não pode ser negativo.')
        return desconto
