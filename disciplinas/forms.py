from django import forms
from django.core.exceptions import ValidationError

from .models import Disciplina

WIDGET_ATTRS = {'class': 'form-control-modern'}


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'carga_horaria', 'descricao', 'obrigatoria']
        widgets = {
            'nome': forms.TextInput(attrs=WIDGET_ATTRS),
            'carga_horaria': forms.NumberInput(attrs=WIDGET_ATTRS),
            'descricao': forms.Textarea(attrs=WIDGET_ATTRS),
            'obrigatoria': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_carga_horaria(self):
        carga = self.cleaned_data['carga_horaria']
        if carga <= 0:
            raise ValidationError('A carga horária deve ser maior que zero.')
        return carga
