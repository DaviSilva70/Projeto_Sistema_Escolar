from django import forms

from .models import Frequencia

WIDGET_ATTRS = {'class': 'form-control-modern'}


class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = ['aluno', 'turma', 'data', 'status', 'justificativa']
        exclude = ['registrado_por']
        widgets = {
            'aluno': forms.Select(attrs=WIDGET_ATTRS),
            'turma': forms.Select(attrs=WIDGET_ATTRS),
            'data': forms.DateInput(attrs={**WIDGET_ATTRS, 'type': 'date'}),
            'status': forms.Select(attrs=WIDGET_ATTRS),
            'justificativa': forms.Textarea(attrs=WIDGET_ATTRS),
        }
