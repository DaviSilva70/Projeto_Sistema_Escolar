from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import User
from .models import Professor


def cadastro_professor_publico(request):
    """Cadastro público de professor - acessível sem login"""
    if request.method == 'POST':
        try:
            user = User.objects.create_user(
                username=request.POST.get('matricula'),
                email=request.POST.get('email', ''),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                tipo='professor',
                telefone=request.POST.get('telefone', ''),
                data_nascimento=request.POST.get('data_nascimento') or None,
                foto=request.FILES.get('foto'),
            )
            Professor.objects.create(
                user=user,
                matricula=request.POST.get('matricula'),
                cpf=request.POST.get('cpf'),
                formacao=request.POST.get('formacao'),
                especialidade=request.POST.get('especialidade', ''),
                data_admissao=request.POST.get('data_admissao'),
                salario=request.POST.get('salario', 0),
            )
            messages.success(request, 'Conta criada com sucesso! Faça login para acessar o sistema.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar: {str(e)}')

    return render(request, 'professores/cadastro_publico.html')


@login_required
def lista_professores(request):
    professores = Professor.objects.filter(ativo=True)
    return render(request, 'professores/lista.html', {'professores': professores})


@login_required
def cadastro_professor(request):
    if request.method == 'POST':
        try:
            user = User.objects.create_user(
                username=request.POST.get('matricula'),
                email=request.POST.get('email', ''),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                tipo='professor',
                telefone=request.POST.get('telefone', ''),
                data_nascimento=request.POST.get('data_nascimento') or None,
                foto=request.FILES.get('foto'),
            )
            Professor.objects.create(
                user=user,
                matricula=request.POST.get('matricula'),
                cpf=request.POST.get('cpf'),
                formacao=request.POST.get('formacao'),
                especialidade=request.POST.get('especialidade', ''),
                data_admissao=request.POST.get('data_admissao'),
                salario=request.POST.get('salario'),
            )
            messages.success(request, f'Professor {user.get_full_name()} cadastrado com sucesso!')
            return redirect('lista_professores')
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar professor: {str(e)}')

    return render(request, 'professores/cadastro.html')


@login_required
def detalhe_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, 'professores/detalhe.html', {'professor': professor})


@login_required
def editar_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)

    if request.method == 'POST':
        try:
            professor.matricula = request.POST.get('matricula', professor.matricula)
            professor.cpf = request.POST.get('cpf', professor.cpf)
            professor.formacao = request.POST.get('formacao', professor.formacao)
            professor.especialidade = request.POST.get('especialidade', professor.especialidade)
            professor.data_admissao = request.POST.get('data_admissao', professor.data_admissao)
            professor.salario = request.POST.get('salario', professor.salario)
            professor.save()

            user = professor.user
            user.first_name = request.POST.get('first_name', user.first_name)
            user.last_name = request.POST.get('last_name', user.last_name)
            user.email = request.POST.get('email', user.email)
            user.telefone = request.POST.get('telefone', user.telefone)
            user.save()

            messages.success(request, f'Professor {user.get_full_name()} atualizado com sucesso!')
            return redirect('detalhe_professor', pk=pk)
        except Exception as e:
            messages.error(request, f'Erro ao atualizar professor: {str(e)}')

    return render(request, 'professores/editar.html', {'professor': professor})
