from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView as BaseLoginView
from django.views import View
from django.contrib import messages


class LoginView(BaseLoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        destinos = {
            'admin': 'dashboard',
            'diretor': 'dashboard',
            'professor': 'dashboard',
            'aluno': 'dashboard',
            'responsavel': 'dashboard',
            'funcionario': 'dashboard',
        }
        destino = destinos.get(user.tipo, 'dashboard')
        return redirect(destino)


def logout_view(request):
    """View de logout que aceita GET"""
    logout(request)
    return redirect('login')


class DashboardView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        from alunos.models import Aluno
        from professores.models import Professor
        from turmas.models import Turma
        from disciplinas.models import Disciplina
        from comunicados.models import Comunicado

        context = {
            'user': request.user,
            'total_alunos': Aluno.objects.filter(ativo=True).count(),
            'total_professores': Professor.objects.filter(ativo=True).count(),
            'total_turmas': Turma.objects.filter(ativo=True).count(),
            'total_disciplinas': Disciplina.objects.filter(ativo=True).count(),
            'total_comunicados': Comunicado.objects.count(),
        }
        return render(request, 'dashboard.html', context)
