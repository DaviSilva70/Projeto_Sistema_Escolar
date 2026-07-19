import secrets
import string

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator
from .models import Professor
from .forms import ProfessorCadastroForm, ProfessorEditarForm
from accounts.models import User
from core.utils.permissoes import perfil_requerido


def _gerar_senha(length=12):
    """Gera senha segura: maiúscula + minúscula + dígito + especial."""
    while True:
        pw = ''.join(secrets.choice(string.ascii_letters + string.digits + '!@#$%&*') for _ in range(length))
        if (any(c.isupper() for c in pw) and any(c.islower() for c in pw)
                and any(c.isdigit() for c in pw) and any(c in '!@#$%&*' for c in pw)):
            return pw


def cadastro_professor_publico(request):
    """Cadastro público de professor - acessível sem login"""
    if request.method == 'POST':
        form = ProfessorCadastroForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                senha = _gerar_senha()
                user = User.objects.create_user(
                    username=cd['matricula'], email=cd.get('email', ''),
                    first_name=cd['first_name'], last_name=cd['last_name'],
                    password=senha,
                    tipo='professor', telefone=cd.get('telefone', ''),
                    data_nascimento=cd.get('data_nascimento'),
                    foto=request.FILES.get('foto'),
                )
                Professor.objects.create(
                    user=user, matricula=cd['matricula'], cpf=cd['cpf'],
                    formacao=cd['formacao'], especialidade=cd.get('especialidade', ''),
                    data_admissao=cd['data_admissao'], salario=cd['salario'],
                )
                messages.success(request,
                    f'Conta criada com sucesso! '
                    f'Seu login: <strong>{cd["matricula"]}</strong> '
                    f'| Senha: <strong>{senha}</strong>. '
                    f'Faça login para acessar o sistema.')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'Já existe um professor com essa matrícula ou CPF.')
            except Exception as e:
                messages.error(request, f'Erro ao cadastrar: {str(e)}')
    else:
        form = ProfessorCadastroForm()
    return render(request, 'professores/cadastro_publico.html', {'form': form})


@perfil_requerido('admin', 'diretor')
def lista_professores(request):
    professores_list = Professor.objects.filter(ativo=True)
    paginator = Paginator(professores_list, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'professores/lista.html', {'page_obj': page_obj})


@perfil_requerido('admin', 'diretor')
def cadastro_professor(request):
    if request.method == 'POST':
        form = ProfessorCadastroForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                senha = _gerar_senha()
                user = User.objects.create_user(
                    username=cd['matricula'], email=cd.get('email', ''),
                    first_name=cd['first_name'], last_name=cd['last_name'],
                    password=senha,
                    tipo='professor', telefone=cd.get('telefone', ''),
                    data_nascimento=cd.get('data_nascimento'),
                    foto=request.FILES.get('foto'),
                )
                Professor.objects.create(
                    user=user, matricula=cd['matricula'], cpf=cd['cpf'],
                    formacao=cd['formacao'], especialidade=cd.get('especialidade', ''),
                    data_admissao=cd['data_admissao'], salario=cd['salario'],
                )
                messages.success(request,
                    f'Professor {user.get_full_name()} cadastrado com sucesso! '
                    f'Login: <strong>{cd["matricula"]}</strong> | Senha: <strong>{senha}</strong>')
                return redirect('lista_professores')
            except IntegrityError:
                messages.error(request, 'Já existe um professor com essa matrícula ou CPF.')
            except Exception as e:
                messages.error(request, f'Erro ao cadastrar professor: {str(e)}')
    else:
        form = ProfessorCadastroForm()
    return render(request, 'professores/cadastro.html', {'form': form})


@perfil_requerido('admin', 'diretor')
def detalhe_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, 'professores/detalhe.html', {'professor': professor})


@perfil_requerido('admin', 'diretor')
def editar_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)

    if request.method == 'POST':
        form = ProfessorEditarForm(request.POST, request.FILES, instance=professor)
        if form.is_valid():
            try:
                professor = form.save(commit=False)
                user = professor.user
                cd = form.cleaned_data
                user.first_name = cd['first_name']
                user.last_name = cd['last_name']
                user.email = cd.get('email', '')
                user.telefone = cd.get('telefone', '')
                if 'foto' in request.FILES:
                    user.foto = request.FILES['foto']
                user.save()
                professor.save()

                messages.success(request, f'Professor {user.get_full_name()} atualizado com sucesso!')
                return redirect('detalhe_professor', pk=pk)
            except IntegrityError:
                messages.error(request, 'Já existe um professor com essa matrícula ou CPF.')
            except Exception as e:
                messages.error(request, f'Erro ao atualizar professor: {str(e)}')
    else:
        form = ProfessorEditarForm(instance=professor)

    return render(request, 'professores/editar.html', {'form': form, 'professor': professor})
