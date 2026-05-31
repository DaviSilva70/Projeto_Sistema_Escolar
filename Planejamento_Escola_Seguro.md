# 📚 Planejamento Seguro - Sistema de Gestão Escolar em Django

## 📋 Informações do Projeto
| Campo | Valor |
|-------|-------|
| **Nome** | Sistema de Gestão Escolar |
| **Banco de Dados** | bd_escola (PostgreSQL) |
| **Framework** | Django 5.x |
| **Python** | 3.12+ |
| **Ambiente** | Windows |

---

## 🗄️ Configuração do Banco de Dados

```python
# config/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bd_escola',
        'USER': 'postgres',
        'PASSWORD': 'sua_senha_aqui',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Comando para criar o banco (PostgreSQL):
```sql
CREATE DATABASE bd_escola;
```

---

## 📦 Dependências (requirements.txt)

```
Django>=5.0
djangorestframework>=3.14
django-crispy-forms>=2.0
crispy-bootstrap5>=0.7
Pillow>=10.0
reportlab>=4.0
django-import-export>=3.2
python-decouple>=3.8
gunicorn>=21.2
psycopg2-binary>=2.9
whitenoise>=6.5
```

---

## 🏗️ Estrutura de Apps

| App | Função | Status |
|-----|--------|--------|
| `config` | Configurações do projeto | ✅ Criado |
| `core` | Modelos base, utilitários | ⏳ Pendente |
| `accounts` | Usuários, autenticação, perfis | ⏳ Pendente |
| `alunos` | Cadastro de alunos | ⏳ Pendente |
| `professores` | Cadastro de professores | ⏳ Pendente |
| `turmas` | Gestão de turmas e séries | ⏳ Pendente |
| `disciplinas` | Disciplinas e grade horária | ⏳ Pendente |
| `notas` | Notas e boletins | ⏳ Pendente |
| `frequencia` | Controle de frequência | ⏳ Pendente |
| `financeiro` | Mensalidades e pagamentos | ⏳ Pendente |
| `comunicados` | Comunicados e notificações | ⏳ Pendente |
| `relatorios` | Relatórios e estatísticas | ⏳ Pendente |
| `agenda` | Calendário e eventos | ⏳ Pendente |

---

## 🔐 Modelo de Usuário Customizado

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    TIPO_CHOICES = [
        ('admin', 'Administrador'),
        ('diretor', 'Diretor'),
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
        ('responsavel', 'Responsável'),
        ('funcionario', 'Funcionário'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    telefone = models.CharField(max_length=20, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    ativo = models.BooleanField(default=True)
```

---

## 📊 Modelos Principais

### Aluno
- user (OneToOne → User)
- ra (Registro do Aluno - único)
- cpf, rg, data_nascimento
- endereco
- responsavel (ForeignKey → User)
- foto, ativo

### Professor
- user (OneToOne → User)
- matricula (única)
- cpf, formacao, especialidade
- data_admissao, salario
- ativo

### Turma
- nome, nivel (Fundamental I/II, Médio)
- serie, turno (manhã/tarde/noite)
- ano_letivo, capacidade, sala

### Disciplina
- nome, carga_horaria
- descricao, obrigatoria

### Nota
- aluno, disciplina, turma
- bimestre (1-4)
- tipo_avaliacao (prova/trabalho/atividade/participacao)
- nota, peso, data_avaliacao

### Frequencia
- aluno, turma, data
- status (P/F/J/A)
- justificativa, registrado_por

### Mensalidade
- aluno, valor
- data_vencimento, data_pagamento
- status (pendente/pago/atrasado/isento)
- desconto, observacao

### Comunicado
- titulo, mensagem, prioridade
- data_criacao, data_validade
- autor, turmas, para_todos

### Evento
- titulo, descricao
- data_inicio, data_fim
- local, responsavel, turmas, cor

---

## 🚀 Comandos Iniciais

```bash
# Ativar ambiente virtual
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Criar projeto Django
django-admin startproject config .

# Criar apps
python manage.py startapp core
python manage.py startapp accounts
python manage.py startapp alunos
python manage.py startapp professores
python manage.py startapp turmas
python manage.py startapp disciplinas
python manage.py startapp notas
python manage.py startapp frequencia
python manage.py startapp financeiro
python manage.py startapp comunicados
python manage.py startapp relatorios
python manage.py startapp agenda

# Criar banco (PostgreSQL)
# CREATE DATABASE bd_escola;

# Executar migrations
python manage.py makemigrations
python manage.py migrate

# Criar superuser
python manage.py createsuperuser

# Rodar servidor
python manage.py runserver
```

---

## 📅 Cronograma de Desenvolvimento

| Fase | Descrição | Semana |
|------|-----------|--------|
| 1 | Configuração inicial, projeto, banco | 1 |
| 2 | Modelos core, accounts, alunos, professores | 2 |
| 3 | Turmas, disciplinas, vinculações | 3 |
| 4 | Notas, frequência, boletins | 4 |
| 5 | Financeiro, comunicados | 5 |
| 6 | Relatórios, dashboard | 6 |
| 7 | UI/UX, testes, deploy | 7 |

---

**Versão: 1.0 | Data: Maio/2026**
