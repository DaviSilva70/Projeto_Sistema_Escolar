import re
from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from .models import Aluno, Responsavel

WIDGET_ATTRS = {'class': 'form-control-modern'}


class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = [
            'tipo', 'nome_completo', 'cpf', 'telefone',
            'email', 'endereco', 'profissao',
        ]
        widgets = {f: forms.TextInput(attrs=WIDGET_ATTRS) for f in fields}
        widgets['endereco'] = forms.Textarea(attrs=WIDGET_ATTRS)
        widgets['tipo'] = forms.Select(attrs=WIDGET_ATTRS)

    def clean_cpf(self):
        cpf = re.sub(r'[.\-]', '', self.cleaned_data['cpf'])
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValidationError('CPF deve conter exatamente 11 dígitos.')
        return cpf

    def clean_telefone(self):
        telefone = re.sub(r'[^\d]', '', self.cleaned_data['telefone'])
        return telefone


class AlunoCadastroForm(forms.Form):
    DATE_FORMATS = ['%d/%m/%Y', '%Y-%m-%d']

    # Dados do usuário
    first_name = forms.CharField(label='Nome', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    last_name = forms.CharField(label='Sobrenome', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    email = forms.EmailField(label='E-mail', required=False, widget=forms.EmailInput(attrs=WIDGET_ATTRS))
    telefone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    data_nascimento = forms.DateField(
        label='Data de Nascimento',
        input_formats=DATE_FORMATS,
        widget=forms.DateInput(attrs={**WIDGET_ATTRS, 'placeholder': 'dd/mm/aaaa', 'type': 'text'})
    )
    foto = forms.FileField(label='Foto', required=False, widget=forms.FileInput(attrs=WIDGET_ATTRS))

    # Dados do aluno
    ra = forms.CharField(label='RA', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    cpf = forms.CharField(label='CPF', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    rg = forms.CharField(label='RG', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    endereco = forms.CharField(label='Endereço do Aluno', required=False, widget=forms.Textarea(attrs=WIDGET_ATTRS))

    # Dados do responsável
    tipo_responsavel = forms.CharField(label='Parentesco', widget=forms.Select(
        attrs=WIDGET_ATTRS,
        choices=[('', 'Selecione o parentesco')] + Responsavel.TIPO_CHOICES
    ))
    nome_responsavel = forms.CharField(label='Nome do Responsável', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    cpf_responsavel = forms.CharField(label='CPF do Responsável', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    telefone_responsavel = forms.CharField(label='Telefone do Responsável', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    email_responsavel = forms.CharField(label='E-mail do Responsável', required=False, widget=forms.EmailInput(attrs=WIDGET_ATTRS))
    endereco_responsavel = forms.CharField(label='Endereço do Responsável', widget=forms.Textarea(attrs=WIDGET_ATTRS))
    profissao_responsavel = forms.CharField(label='Profissão do Responsável', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))

    def clean_ra(self):
        ra = self.cleaned_data['ra'].strip()
        if not ra:
            raise ValidationError('O Registro do Aluno (RA) é obrigatório.')
        return ra

    def clean_cpf(self):
        cpf = re.sub(r'[.\-]', '', self.cleaned_data['cpf'])
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValidationError('CPF deve conter exatamente 11 dígitos.')
        return cpf

    def clean_cpf_responsavel(self):
        cpf = re.sub(r'[.\-]', '', self.cleaned_data['cpf_responsavel'])
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValidationError('CPF do responsável deve conter exatamente 11 dígitos.')
        return cpf

    def clean_data_nascimento(self):
        data = self.cleaned_data['data_nascimento']
        if data > date.today():
            raise ValidationError('A data de nascimento não pode ser no futuro.')
        return data
class AlunoEditarForm(forms.Form):
    DATE_FORMATS = ['%d/%m/%Y', '%Y-%m-%d']

    # Dados do usuário
    first_name = forms.CharField(label='Nome', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    last_name = forms.CharField(label='Sobrenome', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    email = forms.EmailField(label='E-mail', required=False, widget=forms.EmailInput(attrs=WIDGET_ATTRS))
    telefone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    data_nascimento = forms.DateField(
        label='Data de Nascimento', required=False,
        input_formats=DATE_FORMATS,
        widget=forms.DateInput(attrs={**WIDGET_ATTRS, 'placeholder': 'dd/mm/aaaa', 'type': 'text'})
    )
    foto = forms.FileField(label='Foto', required=False, widget=forms.FileInput(attrs=WIDGET_ATTRS))

    # Dados do aluno
    ra = forms.CharField(label='RA', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    cpf = forms.CharField(label='CPF', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    rg = forms.CharField(label='RG', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    endereco = forms.CharField(label='Endereço do Aluno', required=False, widget=forms.Textarea(attrs=WIDGET_ATTRS))

    # Dados do responsável
    tipo_responsavel = forms.CharField(label='Parentesco', required=False, widget=forms.Select(
        attrs=WIDGET_ATTRS,
        choices=[('', 'Selecione o parentesco')] + Responsavel.TIPO_CHOICES
    ))
    nome_responsavel = forms.CharField(label='Nome do Responsável', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    cpf_responsavel = forms.CharField(label='CPF do Responsável', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    telefone_responsavel = forms.CharField(label='Telefone do Responsável', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    email_responsavel = forms.CharField(label='E-mail do Responsável', required=False, widget=forms.EmailInput(attrs=WIDGET_ATTRS))
    endereco_responsavel = forms.CharField(label='Endereço do Responsável', required=False, widget=forms.Textarea(attrs=WIDGET_ATTRS))
    profissao_responsavel = forms.CharField(label='Profissão do Responsável', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))

    # Controle
    ativo = forms.BooleanField(label='Ativo', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def clean_ra(self):
        ra = self.cleaned_data.get('ra', '').strip()
        if ra and not ra:
            raise ValidationError('O Registro do Aluno (RA) não pode ser vazio.')
        return ra

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf', '').strip()
        if not cpf:
            return cpf
        cpf = re.sub(r'[.\-]', '', cpf)
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValidationError('CPF deve conter exatamente 11 dígitos.')
        return cpf

    def clean_cpf_responsavel(self):
        cpf = self.cleaned_data.get('cpf_responsavel', '').strip()
        if not cpf:
            return cpf
        cpf = re.sub(r'[.\-]', '', cpf)
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValidationError('CPF do responsável deve conter exatamente 11 dígitos.')
        return cpf

    def clean_data_nascimento(self):
        data = self.cleaned_data.get('data_nascimento')
        if data and data > date.today():
            raise ValidationError('A data de nascimento não pode ser no futuro.')
        return data
