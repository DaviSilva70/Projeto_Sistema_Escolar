import secrets
import string

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator
from .models import Aluno, Responsavel
from .forms import ResponsavelForm, AlunoCadastroForm, AlunoEditarForm
from accounts.models import User
from core.utils.permissoes import perfil_requerido


def _gerar_senha(length=12):
    """Gera senha segura: maiúscula + minúscula + dígito + especial."""
    while True:
        pw = ''.join(secrets.choice(string.ascii_letters + string.digits + '!@#$%&*') for _ in range(length))
        if (any(c.isupper() for c in pw) and any(c.islower() for c in pw)
                and any(c.isdigit() for c in pw) and any(c in '!@#$%&*' for c in pw)):
            return pw


def cadastro_aluno_publico(request):
    """Cadastro público de aluno - acessível sem login"""
    if request.method == 'POST':
        form = AlunoCadastroForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                responsavel = Responsavel.objects.create(
                    tipo=cd['tipo_responsavel'],
                    nome_completo=cd['nome_responsavel'],
                    cpf=cd['cpf_responsavel'],
                    telefone=cd['telefone_responsavel'],
                    email=cd.get('email_responsavel', ''),
                    endereco=cd['endereco_responsavel'],
                    profissao=cd.get('profissao_responsavel', ''),
                )
                senha = _gerar_senha()
                user = User.objects.create_user(
                    username=cd['ra'],
                    email=cd.get('email', ''),
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    password=senha,
                    tipo='aluno',
                    telefone=cd.get('telefone', ''),
                    data_nascimento=cd.get('data_nascimento'),
                    foto=request.FILES.get('foto'),
                )
                Aluno.objects.create(
                    user=user,
                    ra=cd['ra'],
                    cpf=cd['cpf'],
                    rg=cd.get('rg', ''),
                    data_nascimento=cd['data_nascimento'],
                    endereco=cd.get('endereco', ''),
                    responsavel=responsavel,
                )
                messages.success(request,
                    f'Conta criada com sucesso! '
                    f'Seu login: <strong>{cd["ra"]}</strong> '
                    f'| Senha: <strong>{senha}</strong>. '
                    f'Faça login para acessar o sistema.')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'Erro ao cadastrar: RA ou CPF já cadastrado no sistema.')
    else:
        form = AlunoCadastroForm()
    return render(request, 'alunos/cadastro_publico.html', {'form': form})


@perfil_requerido('admin', 'diretor')
def lista_alunos(request):
    alunos_list = Aluno.objects.filter(ativo=True)
    paginator = Paginator(alunos_list, 15)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'alunos/lista.html', {'alunos': page_obj})


@perfil_requerido('admin', 'diretor')
def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoCadastroForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                responsavel = Responsavel.objects.create(
                    tipo=cd['tipo_responsavel'],
                    nome_completo=cd['nome_responsavel'],
                    cpf=cd['cpf_responsavel'],
                    telefone=cd['telefone_responsavel'],
                    email=cd.get('email_responsavel', ''),
                    endereco=cd['endereco_responsavel'],
                    profissao=cd.get('profissao_responsavel', ''),
                )
                senha = _gerar_senha()
                user = User.objects.create_user(
                    username=cd['ra'],
                    email=cd.get('email', ''),
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    password=senha,
                    tipo='aluno',
                    telefone=cd.get('telefone', ''),
                    data_nascimento=cd.get('data_nascimento'),
                    foto=request.FILES.get('foto'),
                )
                Aluno.objects.create(
                    user=user,
                    ra=cd['ra'],
                    cpf=cd['cpf'],
                    rg=cd.get('rg', ''),
                    data_nascimento=cd['data_nascimento'],
                    endereco=cd.get('endereco', ''),
                    responsavel=responsavel,
                )
                messages.success(request,
                    f'Aluno {user.get_full_name()} cadastrado com sucesso! '
                    f'Login: <strong>{cd["ra"]}</strong> | Senha: <strong>{senha}</strong>')
                return redirect('lista_alunos')
            except IntegrityError:
                messages.error(request, 'Erro ao cadastrar aluno: RA ou CPF já cadastrado no sistema.')
    else:
        form = AlunoCadastroForm()
    return render(request, 'alunos/cadastro.html', {'form': form, 'responsaveis': Responsavel.objects.all()})


@perfil_requerido('admin', 'diretor')
def detalhe_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'alunos/detalhe.html', {'aluno': aluno})


@perfil_requerido('admin', 'diretor')
def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    responsavel = aluno.responsavel
    user = aluno.user

    if request.method == 'POST':
        form = AlunoEditarForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                responsavel.tipo = cd.get('tipo_responsavel', responsavel.tipo)
                responsavel.nome_completo = cd.get('nome_responsavel', responsavel.nome_completo)
                responsavel.cpf = cd.get('cpf_responsavel', responsavel.cpf)
                responsavel.telefone = cd.get('telefone_responsavel', responsavel.telefone)
                responsavel.email = cd.get('email_responsavel', responsavel.email)
                responsavel.endereco = cd.get('endereco_responsavel', responsavel.endereco)
                responsavel.profissao = cd.get('profissao_responsavel', responsavel.profissao)
                responsavel.save()

                aluno.ra = cd.get('ra', aluno.ra)
                aluno.cpf = cd.get('cpf', aluno.cpf)
                aluno.rg = cd.get('rg', aluno.rg)
                if cd.get('data_nascimento'):
                    aluno.data_nascimento = cd['data_nascimento']
                aluno.endereco = cd.get('endereco', aluno.endereco)
                aluno.ativo = cd.get('ativo', aluno.ativo)
                aluno.save()

                user.first_name = cd.get('first_name', user.first_name)
                user.last_name = cd.get('last_name', user.last_name)
                user.email = cd.get('email', user.email)
                user.telefone = cd.get('telefone', user.telefone)
                if request.FILES.get('foto'):
                    user.foto = request.FILES['foto']
                user.save()

                messages.success(request, f'Aluno {user.get_full_name()} atualizado com sucesso!')
                return redirect('detalhe_aluno', pk=pk)
            except IntegrityError:
                messages.error(request, 'Erro ao atualizar aluno: RA ou CPF já cadastrado no sistema.')
    else:
        initial = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'telefone': user.telefone,
            'data_nascimento': aluno.data_nascimento.strftime('%d/%m/%Y') if aluno.data_nascimento else '',
            'ra': aluno.ra,
            'cpf': aluno.cpf,
            'rg': aluno.rg,
            'endereco': aluno.endereco,
            'ativo': aluno.ativo,
            'tipo_responsavel': responsavel.tipo,
            'nome_responsavel': responsavel.nome_completo,
            'cpf_responsavel': responsavel.cpf,
            'telefone_responsavel': responsavel.telefone,
            'email_responsavel': responsavel.email,
            'endereco_responsavel': responsavel.endereco,
            'profissao_responsavel': responsavel.profissao,
        }
        form = AlunoEditarForm(initial=initial)
    return render(request, 'alunos/editar.html', {'aluno': aluno, 'form': form})


@perfil_requerido('admin', 'diretor')
def lista_responsaveis(request):
    responsaveis_list = Responsavel.objects.all()
    paginator = Paginator(responsaveis_list, 15)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'alunos/lista_responsaveis.html', {'responsaveis': page_obj})


@perfil_requerido('admin', 'diretor')
def cadastro_responsavel(request):
    if request.method == 'POST':
        form = ResponsavelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Responsável cadastrado com sucesso!')
                return redirect('lista_responsaveis')
            except IntegrityError:
                messages.error(request, 'Erro ao cadastrar responsável: CPF já cadastrado no sistema.')
    else:
        form = ResponsavelForm()
    return render(request, 'alunos/cadastro_responsavel.html', {'form': form})


@perfil_requerido('admin', 'diretor')
def editar_responsavel(request, pk):
    responsavel = get_object_or_404(Responsavel, pk=pk)
    if request.method == 'POST':
        form = ResponsavelForm(request.POST, instance=responsavel)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Responsável atualizado com sucesso!')
                return redirect('lista_responsaveis')
            except IntegrityError:
                messages.error(request, 'Erro ao atualizar responsável: CPF já cadastrado no sistema.')
    else:
        form = ResponsavelForm(instance=responsavel)
    return render(request, 'alunos/editar_responsavel.html', {'responsavel': responsavel, 'form': form})


@perfil_requerido('admin', 'diretor')
def excluir_responsavel(request, pk):
    responsavel = get_object_or_404(Responsavel, pk=pk)
    if request.method == 'POST':
        try:
            responsavel.delete()
            messages.success(request, 'Responsável excluído com sucesso!')
        except IntegrityError:
            messages.error(request, 'Erro ao excluir responsável: existem alunos vinculados a este responsável.')
        return redirect('lista_responsaveis')
    return render(request, 'alunos/confirmar_exclusao_responsavel.html', {'responsavel': responsavel})
