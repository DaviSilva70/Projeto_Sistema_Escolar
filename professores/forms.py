import re

from django import forms
from django.core.exceptions import ValidationError

WIDGET_ATTRS = {'class': 'form-control-modern'}


class ProfessorCadastroForm(forms.Form):
    DATE_FORMATS = ['%d/%m/%Y', '%Y-%m-%d']

    # Dados do usuário
    first_name = forms.CharField(label='Nome', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    last_name = forms.CharField(label='Sobrenome', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    email = forms.EmailField(label='E-mail', required=False, widget=forms.EmailInput(attrs=WIDGET_ATTRS))
    telefone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    data_nascimento = forms.DateField(label='Data de Nascimento', required=False,
        input_formats=DATE_FORMATS,
        widget=forms.DateInput(attrs={**WIDGET_ATTRS, 'placeholder': 'dd/mm/aaaa', 'type': 'text'})
    )
    foto = forms.FileField(label='Foto', required=False, widget=forms.FileInput(attrs=WIDGET_ATTRS))

    # Dados do professor
    matricula = forms.CharField(label='Matrícula', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    cpf = forms.CharField(label='CPF', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    formacao = forms.CharField(label='Formação', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    especialidade = forms.CharField(label='Especialidade', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    data_admissao = forms.DateField(label='Data de Admissão',
        input_formats=DATE_FORMATS,
        widget=forms.DateInput(attrs={**WIDGET_ATTRS, 'placeholder': 'dd/mm/aaaa', 'type': 'text'})
    )
    salario = forms.DecimalField(label='Salário', max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs=WIDGET_ATTRS))
    last_name = forms.CharField(label='Sobrenome', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    email = forms.EmailField(label='E-mail', required=False, widget=forms.EmailInput(attrs=WIDGET_ATTRS))
    telefone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    data_nascimento = forms.DateField(label='Data de Nascimento', required=False, widget=forms.DateInput(attrs={**WIDGET_ATTRS, 'type': 'date'}))
    foto = forms.FileField(label='Foto', required=False, widget=forms.FileInput(attrs=WIDGET_ATTRS))

    # Dados do professor
    matricula = forms.CharField(label='Matrícula', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    cpf = forms.CharField(label='CPF', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    formacao = forms.CharField(label='Formação', widget=forms.TextInput(attrs=WIDGET_ATTRS))
    especialidade = forms.CharField(label='Especialidade', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    data_admissao = forms.DateField(label='Data de Admissão', widget=forms.DateInput(attrs={**WIDGET_ATTRS, 'type': 'date'}))
    salario = forms.DecimalField(label='Salário', max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs=WIDGET_ATTRS))

    def clean_cpf(self):
        cpf = re.sub(r'[.\-]', '', self.cleaned_data['cpf'])
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValidationError('CPF deve conter exatamente 11 dígitos.')
        return cpf

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula'].strip()
        if not matricula:
            raise ValidationError('A matrícula é obrigatória.')
        return matricula

    def clean_salario(self):
        salario = self.cleaned_data['salario']
        if salario <= 0:
            raise ValidationError('O salário deve ser maior que zero.')
        return salario


class ProfessorEditarForm(forms.Form):
    # Dados do usuário
    first_name = forms.CharField(label='Nome', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    last_name = forms.CharField(label='Sobrenome', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    email = forms.EmailField(label='E-mail', required=False, widget=forms.EmailInput(attrs=WIDGET_ATTRS))
    telefone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    data_nascimento = forms.DateField(label='Data de Nascimento', required=False,
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={**WIDGET_ATTRS, 'placeholder': 'dd/mm/aaaa', 'type': 'text'})
    )
    # Dados do professor
    matricula = forms.CharField(label='Matrícula', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    cpf = forms.CharField(label='CPF', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    formacao = forms.CharField(label='Formação', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    especialidade = forms.CharField(label='Especialidade', required=False, widget=forms.TextInput(attrs=WIDGET_ATTRS))
    data_admissao = forms.DateField(label='Data de Admissão', required=False,
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={**WIDGET_ATTRS, 'placeholder': 'dd/mm/aaaa', 'type': 'text'})
    )
    salario = forms.DecimalField(label='Salário', required=False, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs=WIDGET_ATTRS))

    # Controle
    ativo = forms.BooleanField(label='Ativo', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf', '').strip()
        if not cpf:
            return cpf
        cpf = re.sub(r'[.\-]', '', cpf)
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValidationError('CPF deve conter exatamente 11 dígitos.')
        return cpf

    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula', '').strip()
        if matricula and not matricula:
            raise ValidationError('A matrícula não pode ser vazia.')
        return matricula

    def clean_salario(self):
        salario = self.cleaned_data.get('salario')
        if salario is not None and salario <= 0:
            raise ValidationError('O salário deve ser maior que zero.')
        return salario
