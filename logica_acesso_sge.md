# Lógica de Controle de Acesso — Sistema de Gestão Escolar (SGE)

> **Projeto:** Bem-vindo ao Sistema de Gestão Escolar  
> **Framework:** Django  
> **Autor:** David — Centro Universitário Unidombosco  

---

## 1. Visão Geral dos Perfis (Roles)

| Perfil        | Descrição                                      |
|---------------|------------------------------------------------|
| `admin`       | Gestor do sistema (acesso total)               |
| `professor`   | Docente — acessa dados dos seus alunos         |
| `aluno`       | Estudante — acessa apenas seus próprios dados  |

---

## 2. Mapeamento de Permissões por Página

| Página / Recurso        | Admin | Professor           | Aluno          |
|-------------------------|-------|---------------------|----------------|
| Dashboard principal     | ✅    | ✅                  | ✅             |
| **Notas**               | ✅    | ✅ (seus alunos)    | ✅ (suas notas)|
| **Disciplinas**         | ✅    | ✅ (suas turmas)    | ✅ (suas disciplinas) |
| **Frequência**          | ✅    | ✅ (seus alunos)    | ✅ (sua frequência) |
| **Comunicados**         | ✅    | ✅ (ler + criar)    | ✅ (ler)       |
| **Agenda**              | ✅    | ✅ (gerenciar)      | ❌             |
| Gerenciar Usuários      | ✅    | ❌                  | ❌             |
| Relatórios Gerais       | ✅    | ❌                  | ❌             |

---

## 3. Estrutura de Models Sugerida

```python
# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    PERFIS = [
        ('admin', 'Administrador'),
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
    ]
    perfil = models.CharField(max_length=20, choices=PERFIS, default='aluno')

class Professor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField('Disciplina', blank=True)

class Aluno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    turma = models.ForeignKey('Turma', on_delete=models.SET_NULL, null=True)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    bimestre = models.IntegerField()

class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField(default=True)

class Comunicado(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    publico_alvo = models.CharField(
        max_length=20,
        choices=[('todos', 'Todos'), ('alunos', 'Alunos'), ('professores', 'Professores')],
        default='todos'
    )

class Agenda(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    data_evento = models.DateTimeField()
```

---

## 4. Decorators e Mixins de Controle de Acesso

```python
# utils/permissoes.py

from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def perfil_requerido(*perfis):
    """
    Decorator que verifica se o usuário tem o perfil adequado.
    Uso: @perfil_requerido('professor', 'admin')
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped(request, *args, **kwargs):
            if request.user.perfil in perfis:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied  # retorna HTTP 403
        return _wrapped
    return decorator


# Mixins para Class-Based Views (CBV)
from django.contrib.auth.mixins import LoginRequiredMixin

class PerfilMixin(LoginRequiredMixin):
    perfis_permitidos = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.perfil not in self.perfis_permitidos:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
```

---

## 5. Aplicando nas Views

### 5.1 Function-Based Views (FBV)

```python
# views.py

from utils.permissoes import perfil_requerido
from django.contrib.auth.decorators import login_required

# Aluno: ver suas próprias notas
@perfil_requerido('aluno', 'admin')
def minhas_notas(request):
    notas = Nota.objects.filter(aluno=request.user.aluno)
    return render(request, 'notas/minhas_notas.html', {'notas': notas})

# Professor: ver notas dos seus alunos
@perfil_requerido('professor', 'admin')
def notas_turma(request):
    professor = request.user.professor
    notas = Nota.objects.filter(disciplina__professor=professor)
    return render(request, 'notas/notas_turma.html', {'notas': notas})

# Professor: gerenciar agenda
@perfil_requerido('professor', 'admin')
def minha_agenda(request):
    agenda = Agenda.objects.filter(professor=request.user.professor)
    return render(request, 'agenda/agenda.html', {'agenda': agenda})

# Comunicados: acesso para todos logados
@login_required
def comunicados(request):
    perfil = request.user.perfil
    if perfil == 'aluno':
        comunicados = Comunicado.objects.filter(publico_alvo__in=['todos', 'alunos'])
    elif perfil == 'professor':
        comunicados = Comunicado.objects.filter(publico_alvo__in=['todos', 'professores'])
    else:
        comunicados = Comunicado.objects.all()
    return render(request, 'comunicados/lista.html', {'comunicados': comunicados})
```

### 5.2 Class-Based Views (CBV)

```python
from utils.permissoes import PerfilMixin

class FrequenciaAlunoView(PerfilMixin, ListView):
    perfis_permitidos = ['aluno', 'admin']
    template_name = 'frequencia/aluno.html'

    def get_queryset(self):
        return Frequencia.objects.filter(aluno=self.request.user.aluno)


class FrequenciaProfessorView(PerfilMixin, ListView):
    perfis_permitidos = ['professor', 'admin']
    template_name = 'frequencia/professor.html'

    def get_queryset(self):
        return Frequencia.objects.filter(
            disciplina__professor=self.request.user.professor
        )
```

---

## 6. URLs com Proteção

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Rotas do Aluno
    path('aluno/notas/', views.minhas_notas, name='minhas_notas'),
    path('aluno/frequencia/', views.FrequenciaAlunoView.as_view(), name='frequencia_aluno'),
    path('aluno/disciplinas/', views.minhas_disciplinas, name='minhas_disciplinas'),

    # Rotas do Professor
    path('professor/notas/', views.notas_turma, name='notas_turma'),
    path('professor/frequencia/', views.FrequenciaProfessorView.as_view(), name='frequencia_professor'),
    path('professor/agenda/', views.minha_agenda, name='minha_agenda'),

    # Rota compartilhada (aluno + professor)
    path('comunicados/', views.comunicados, name='comunicados'),
]
```

---

## 7. Redirecionamento Pós-Login por Perfil

```python
# views.py — override do login padrão

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redireciona conforme o perfil
            destinos = {
                'admin': '/admin/dashboard/',
                'professor': '/professor/notas/',
                'aluno': '/aluno/notas/',
            }
            return redirect(destinos.get(user.perfil, '/'))
        else:
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})

    return render(request, 'login.html')
```

---

## 8. Tratamento de Acesso Negado (403)

```python
# templates/403.html
```
```html
{% extends "base.html" %}
{% block content %}
<div class="alert alert-danger">
  <h3>Acesso Negado</h3>
  <p>Você não tem permissão para acessar esta página.</p>
  <a href="{% url 'dashboard' %}">Voltar ao início</a>
</div>
{% endblock %}
```

```python
# settings.py
handler403 = 'sge.views.erro_403'
```

---

## 9. Segurança no Template (Ocultar Menus)

```html
<!-- base.html — exibir itens de menu conforme perfil -->
{% if user.perfil == 'professor' or user.perfil == 'admin' %}
  <li><a href="{% url 'agenda' %}">Agenda</a></li>
{% endif %}

{% if user.perfil == 'aluno' %}
  <li><a href="{% url 'minhas_notas' %}">Minhas Notas</a></li>
{% endif %}

{% if user.is_authenticated %}
  <li><a href="{% url 'comunicados' %}">Comunicados</a></li>
{% endif %}
```

> ⚠️ **Importante:** Ocultar no template **não é suficiente**. Sempre proteja também as views com decorators/mixins, pois o usuário pode digitar a URL diretamente.

---

## 10. Fluxo Resumido

```
Login
  ├── perfil == 'admin'      → Dashboard Admin (acesso total)
  ├── perfil == 'professor'  → /professor/notas/
  │       ├── Notas dos seus alunos
  │       ├── Frequência dos seus alunos
  │       ├── Comunicados (ler + criar)
  │       └── Agenda (gerenciar)
  └── perfil == 'aluno'      → /aluno/notas/
          ├── Suas Notas
          ├── Suas Disciplinas
          ├── Sua Frequência
          └── Comunicados (somente leitura)
```

---

## 11. Próximos Passos Sugeridos

- [ ] Implementar `AbstractUser` com campo `perfil` no `settings.py` (`AUTH_USER_MODEL = 'app.Usuario'`)
- [ ] Criar `signals` para gerar automaticamente `Aluno` ou `Professor` ao criar usuário
- [ ] Adicionar testes unitários para cada decorator de permissão
- [ ] Considerar `django-guardian` para permissões por objeto (ex: professor só vê sua própria turma)
- [ ] Proteger a API REST (se houver) com `djangorestframework` + `IsAuthenticated` + permissões customizadas
