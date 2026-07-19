from django import forms

from .models import Comunicado

WIDGET_ATTRS = {'class': 'form-control-modern'}


class ComunicadoForm(forms.ModelForm):
    class Meta:
        model = Comunicado
        fields = ['titulo', 'mensagem', 'prioridade', 'data_validade', 'turmas', 'para_todos']
        exclude = ['autor', 'lido']
        widgets = {
            'titulo': forms.TextInput(attrs=WIDGET_ATTRS),
            'mensagem': forms.Textarea(attrs=WIDGET_ATTRS),
            'prioridade': forms.Select(attrs=WIDGET_ATTRS),
            'data_validade': forms.DateInput(attrs={**WIDGET_ATTRS, 'type': 'date'}),
            'turmas': forms.CheckboxSelectMultiple(),
            'para_todos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
