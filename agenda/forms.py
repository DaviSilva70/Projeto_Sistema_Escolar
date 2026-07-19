from django import forms
from django.core.exceptions import ValidationError

from .models import Evento

WIDGET_ATTRS = {'class': 'form-control-modern'}


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'data_inicio', 'data_fim', 'local', 'turmas', 'cor']
        exclude = ['responsavel']
        widgets = {
            'titulo': forms.TextInput(attrs=WIDGET_ATTRS),
            'descricao': forms.Textarea(attrs=WIDGET_ATTRS),
            'data_inicio': forms.DateTimeInput(attrs={**WIDGET_ATTRS, 'type': 'datetime-local'}),
            'data_fim': forms.DateTimeInput(attrs={**WIDGET_ATTRS, 'type': 'datetime-local'}),
            'local': forms.TextInput(attrs=WIDGET_ATTRS),
            'turmas': forms.CheckboxSelectMultiple(),
            'cor': forms.TextInput(attrs={**WIDGET_ATTRS, 'type': 'color'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')
        if data_inicio and data_fim and data_fim <= data_inicio:
            raise ValidationError('A data/hora de término deve ser posterior à data/hora de início.')
        return cleaned_data
