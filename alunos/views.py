from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Aluno, Responsavel
from accounts.models import User


def cadastro_aluno_publico(request):
    """Cadastro público de aluno - acessível sem login"""
    if request.method == 'POST':
        try:
            # Dados do responsável - SEMPRE criar novo
            responsavel = Responsavel.objects.create(
                tipo=request.POST.get('tipo_responsavel'),
                nome_completo=request.POST.get('nome_responsavel'),
                cpf=request.POST.get('cpf_responsavel'),
                telefone=request.POST.get('telefone_responsavel'),
                endereco=request.POST.get('endereco_responsavel'),
                email=request.POST.get('email_responsavel', ''),
                profissao=request.POST.get('profissao_responsavel', ''),
            )

            # Dados do aluno
            ra = request.POST.get('ra')

            # Criar usuário
            user = User.objects.create_user(
                username=ra,
                email=request.POST.get('email', ''),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                tipo='aluno',
                telefone=request.POST.get('telefone', ''),
                data_nascimento=request.POST.get('data_nascimento') or None,
                foto=request.FILES.get('foto'),
            )

            # Criar aluno
            Aluno.objects.create(
                user=user,
                ra=ra,
                cpf=request.POST.get('cpf'),
                rg=request.POST.get('rg', ''),
                data_nascimento=request.POST.get('data_nascimento'),
                endereco=request.POST.get('endereco', ''),
                responsavel=responsavel,
            )

            messages.success(request, 'Conta criada com sucesso! Faça login para acessar o sistema.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Erro ao cadastrar: {str(e)}')

    return render(request, 'alunos/cadastro_publico.html')


@login_required
def lista_alunos(request):
    alunos = Aluno.objects.filter(ativo=True)
    return render(request, 'alunos/lista.html', {'alunos': alunos})


@login_required
def cadastro_aluno(request):
    responsaveis = Responsavel.objects.all()

    if request.method == 'POST':
        try:
            # Dados do responsável - SEMPRE criar novo
            responsavel = Responsavel.objects.create(
                tipo=request.POST.get('tipo_responsavel'),
                nome_completo=request.POST.get('nome_responsavel'),
                cpf=request.POST.get('cpf_responsavel'),
                telefone=request.POST.get('telefone_responsavel'),
                endereco=request.POST.get('endereco_responsavel'),
                email=request.POST.get('email_responsavel', ''),
                profissao=request.POST.get('profissao_responsavel', ''),
            )

            # Dados do aluno
            ra = request.POST.get('ra')

            # Criar usuário
            user = User.objects.create_user(
                username=ra,
                email=request.POST.get('email', ''),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                tipo='aluno',
                telefone=request.POST.get('telefone', ''),
                data_nascimento=request.POST.get('data_nascimento') or None,
            )

            # Criar aluno
            Aluno.objects.create(
                user=user,
                ra=ra,
                cpf=request.POST.get('cpf'),
                rg=request.POST.get('rg', ''),
                data_nascimento=request.POST.get('data_nascimento'),
                endereco=request.POST.get('endereco', ''),
                responsavel=responsavel,
            )

            messages.success(request, f'Aluno {user.get_full_name()} cadastrado com sucesso!')
            return redirect('lista_alunos')

        except Exception as e:
            messages.error(request, f'Erro ao cadastrar aluno: {str(e)}')

    return render(request, 'alunos/cadastro.html', {'responsaveis': responsaveis})


@login_required
def detalhe_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'alunos/detalhe.html', {'aluno': aluno})


@login_required
def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    responsaveis = Responsavel.objects.all()

    if request.method == 'POST':
        try:
            # Atualizar responsável
            responsavel = aluno.responsavel
            responsavel.tipo = request.POST.get('tipo_responsavel', responsavel.tipo)
            responsavel.nome_completo = request.POST.get('nome_responsavel', responsavel.nome_completo)
            responsavel.cpf = request.POST.get('cpf_responsavel', responsavel.cpf)
            responsavel.telefone = request.POST.get('telefone_responsavel', responsavel.telefone)
            responsavel.endereco = request.POST.get('endereco_responsavel', responsavel.endereco)
            responsavel.email = request.POST.get('email_responsavel', responsavel.email)
            responsavel.profissao = request.POST.get('profissao_responsavel', responsavel.profissao)
            responsavel.save()

            # Atualizar aluno
            aluno.ra = request.POST.get('ra', aluno.ra)
            aluno.cpf = request.POST.get('cpf', aluno.cpf)
            aluno.rg = request.POST.get('rg', aluno.rg)
            aluno.data_nascimento = request.POST.get('data_nascimento', aluno.data_nascimento)
            aluno.endereco = request.POST.get('endereco', aluno.endereco)
            aluno.ativo = request.POST.get('ativo', 'True') == 'True'
            aluno.save()

            # Atualizar usuário
            user = aluno.user
            user.first_name = request.POST.get('first_name', user.first_name)
            user.last_name = request.POST.get('last_name', user.last_name)
            user.email = request.POST.get('email', user.email)
            user.telefone = request.POST.get('telefone', user.telefone)
            user.save()

            messages.success(request, f'Aluno {user.get_full_name()} atualizado com sucesso!')
            return redirect('detalhe_aluno', pk=pk)

        except Exception as e:
            messages.error(request, f'Erro ao atualizar aluno: {str(e)}')

    return render(request, 'alunos/editar.html', {'aluno': aluno, 'responsaveis': responsaveis})
