from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    """Formulário para cadastro e edição de vídeos"""
    class Meta:
        model = Video
        fields = ['titulo', 'descricao', 'url', 'categoria', 'disciplina', 'turmas', 'ativo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control-modern', 'placeholder': 'Título do vídeo'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control-modern', 'rows': 3, 'placeholder': 'Descrição do vídeo'}),
            'url': forms.URLInput(attrs={'class': 'form-control-modern', 'placeholder': 'https://www.youtube.com/watch?v=...'}),
            'categoria': forms.Select(attrs={'class': 'form-control-modern'}),
            'disciplina': forms.Select(attrs={'class': 'form-control-modern'}),
            'turmas': forms.SelectMultiple(attrs={'class': 'form-control-modern'}),
            'ordem': forms.NumberInput(attrs={'class': 'form-control-modern', 'min': '0'}),
        }

    def clean_url(self):
        url = self.cleaned_data.get('url', '')
        if not url:
            raise forms.ValidationError('URL é obrigatória.')
        if 'youtube.com' not in url and 'youtu.be' not in url and 'vimeo.com' not in url:
            raise forms.ValidationError('Apenas URLs do YouTube ou Vimeo são aceitas.')
        return url
