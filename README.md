# 📚 Sistema de Gestão Escolar (SGE)

[![Django](https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.x-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> Sistema completo para gerenciamento escolar com controle de acesso por perfil, cadastro de alunos, professores, turmas, disciplinas, notas, frequência, financeiro e comunicados.

---

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias](#-tecnologias)
- [Instalação](#-instalação)
- [Configuração do Banco](#-configuração-do-banco)
- [Uso](#-uso)
- [Controle de Acesso](#-controle-de-acesso)
- [Models](#-models)
- [API Reference](#-api-reference)
- [Screenshots](#-screenshots)
- [Contribuidores](#-contribuidores)
- [Licença](#-licença)

---

## 🎯 Visão Geral

O **Sistema de Gestão Escolar (SGE)** é uma aplicação web desenvolvida em Django para auxiliar na administração de instituições de ensino. O sistema permite gerenciar alunos, professores, turmas, disciplinas, notas, frequência, financeiro e comunicados de forma integrada e segura.

### Autor
**David Silva** - Centro Universitário Unidombosco

---

## ✨ Funcionalidades

### 🎓 Gestão de Alunos
- Cadastro completo com dados pessoais
- Upload de foto para registro
- Vinculação com responsável (Pai, Mãe, Avô, Avó, Tio, etc.)
- Controle de status (ativo/inativo)
- Busca e filtros

### 👨‍🏫 Gestão de Professores
- Cadastro com dados profissionais
- Formação e especialidade
- Upload de foto
- Vinculação com disciplinas

### 📚 Gestão de Turmas
- Séries e níveis (Fundamental I, II, Médio)
- Turnos (Manhã, Tarde, Noite)
- Capacidade e sala de aula
- Ano letivo

### 📖 Gestão de Disciplinas
- Cadastro de disciplinas
- Carga horária
- Obrigatórias e optativas

### 📝 Sistema de Notas
- Lançamento de notas por bimestre
- Tipos de avaliação (Prova, Trabalho, Atividade, Participação)
- Cálculo automático de médias
- Boletim escolar

### ✅ Controle de Frequência
- Chamada digital
- Registro por aula
- Justificativas de ausência
- Histórico de frequência

### 💰 Gestão Financeira
- Mensalidades
- Controle de pagamentos
- Status (Pago, Pendente, Atrasado, Isento)

### 📢 Comunicados
- Avisos gerais e por turma
- Prioridade (Baixa, Média, Alta)
- Data de validade

### 📅 Agenda
- Calendário de eventos
- Eventos por turma
- Cores personalizadas

### 📊 Relatórios
- Dashboard administrativo
- Estatísticas gerais
- Relatórios de desempenho

---

## 📁 Estrutura do Projeto

```
Projeto_Sistema_Escolar/
├── config/                    # Configurações do projeto
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/                      # Aplicações Django
│   ├── core/                  # Modelos base e utilitários
│   ├── accounts/              # Usuários e autenticação
│   ├── alunos/                # Gestão de alunos
│   ├── professores/           # Gestão de professores
│   ├── turmas/                # Gestão de turmas
│   ├── disciplinas/           # Gestão de disciplinas
│   ├── notas/                 # Notas e boletins
│   ├── frequencia/            # Controle de frequência
│   ├── financeiro/            # Gestão financeira
│   ├── comunicados/           # Comunicados
│   ├── relatorios/            # Relatórios
│   └── agenda/                # Agenda e eventos
│
├── templates/                 # Templates HTML
│   ├── base.html              # Layout principal
│   ├── login.html             # Tela de login
│   ├── dashboard.html         # Painel principal
│   ├── cadastro_perfil.html   # Escolha de perfil
│   ├── 403.html               # Acesso negado
│   ├── alunos/                # Templates de alunos
│   ├── professores/           # Templates de professores
│   ├── turmas/                # Templates de turmas
│   ├── disciplinas/           # Templates de disciplinas
│   ├── notas/                 # Templates de notas
│   ├── frequencia/            # Templates de frequência
│   ├── financeiro/            # Templates financeiros
│   ├── comunicados/           # Templates de comunicados
│   ├── relatorios/            # Templates de relatórios
│   └── agenda/                # Templates de agenda
│
├── static/                    # Arquivos estáticos
│   ├── css/
│   │   └── custom.css         # CSS customizado
│   ├── js/
│   │   └── custom.js          # JavaScript customizado
│   └── img/
│       └── logo.png
│
├── media/                     # Arquivos de mídia
│   └── fotos/                 # Fotos de alunos/professores
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|--------|------------|
| **Backend** | Django 5.x / Python 3.12+ |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Banco de Dados** | MySQL 8.x |
| **Autenticação** | Django Auth + Custom User Model |
| **Administrativo** | Django Admin customizado |
| **Ícones** | Bootstrap Icons |
| **Fonte** | Google Fonts (Inter) |

---

## 🚀 Instalação

### Pré-requisitos
- Python 3.12+
- MySQL 8.x
- pip

### 1. Clone o repositório
```bash
git clone https://github.com/DaviSilva70/Projeto_Sistema_Escolar.git
cd Projeto_Sistema_Escolar
```

### 2. Crie o ambiente virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
# Crie o banco no MySQL
mysql -u root -p
CREATE DATABASE bd_escola CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### 5. Configure as variáveis de ambiente
Edite `config/settings.py` com suas credenciais MySQL:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "bd_escola",
        "USER": "root",
        "PASSWORD": "sua_senha",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

### 6. Execute as migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crie o superuser
```bash
python manage.py createsuperuser
```

### 8. Execute o servidor
```bash
python manage.py runserver
```

---

## 🗄️ Configuração do Banco

### MySQL
```sql
CREATE DATABASE bd_escola 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```

### SQLite (desenvolvimento)
Para usar SQLite, altere `config/settings.py`:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

---

## 📖 Uso

### Acesso ao Sistema
- **URL:** `http://127.0.0.1:8000/`
- **Login:** `http://127.0.0.1:8000/login/`
- **Cadastro:** `http://127.0.0.1:8000/cadastro/`
- **Admin:** `http://127.0.0.1:8000/admin/`

### Fluxo de Cadastro
1. Acesse a tela de login
2. Clique em **"Criar minha conta"**
3. Escolha o perfil (Professor ou Aluno)
4. Preencha os dados e faça upload da foto
5. Após o cadastro, faça login

### Usuários Padrão
| Usuário | Senha | Perfil |
|---------|-------|--------|
| admin | admin123 | Administrador |

---

## 🔐 Controle de Acesso

### Perfis de Usuário

| Perfil | Descrição | Permissões |
|--------|-----------|------------|
| `admin` | Administrador | Acesso total ao sistema |
| `diretor` | Diretor | Acesso administrativo completo |
| `professor` | Professor | Notas, frequência, comunicados, agenda |
| `aluno` | Aluno | Suas notas, frequência, comunicados |
| `responsavel` | Responsável | Dados dos filhos, notas, financeiro |
| `funcionario` | Funcionário | Acesso limitado |

### Mapeamento de Permissões

| Página | Admin | Professor | Aluno |
|--------|-------|-----------|-------|
| Dashboard | ✅ | ✅ | ✅ |
| Alunos | ✅ | ❌ | ❌ |
| Professores | ✅ | ❌ | ❌ |
| Turmas | ✅ | ❌ | ❌ |
| Disciplinas | ✅ | ❌ | ❌ |
| Notas | ✅ | ✅ | ✅ (próprias) |
| Frequência | ✅ | ✅ | ✅ (própria) |
| Agenda | ✅ | ✅ | ❌ |
| Financeiro | ✅ | ❌ | ❌ |
| Comunicados | ✅ | ✅ | ✅ |
| Relatórios | ✅ | ❌ | ❌ |

### Decorator de Permissão
```python
from core.utils.permissoes import perfil_requerido

@perfil_requerido('admin', 'diretor')
def minha_view(request):
    ...
```

---

## 📊 Models

### User (Custom)
```python
class User(AbstractUser):
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='usuarios/')
    ativo = models.BooleanField(default=True)
```

### Aluno
```python
class Aluno(TimeStampedModel):
    user = models.OneToOneField(User)
    ra = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    responsavel = models.ForeignKey(Responsavel)
    foto = models.ImageField(upload_to='alunos/')
```

### Professor
```python
class Professor(TimeStampedModel):
    user = models.OneToOneField(User)
    matricula = models.CharField(max_length=20, unique=True)
    formacao = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    data_admissao = models.DateField()
    salario = models.DecimalField()
```

### Turma
```python
class Turma(TimeStampedModel):
    nome = models.CharField(max_length=50)
    nivel = models.CharField(choices=NIVEL_CHOICES)
    serie = models.IntegerField()
    turno = models.CharField(choices=TURNO_CHOICES)
    ano_letivo = models.IntegerField()
    capacidade = models.IntegerField(default=40)
```

### Disciplina
```python
class Disciplina(TimeStampedModel):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    obrigatoria = models.BooleanField(default=True)
```

### Nota
```python
class Nota(TimeStampedModel):
    aluno = models.ForeignKey(Aluno)
    disciplina = models.ForeignKey(Disciplina)
    turma = models.ForeignKey(Turma)
    bimestre = models.IntegerField()
    nota = models.DecimalField()
    peso = models.DecimalField(default=1.0)
```

### Frequencia
```python
class Frequencia(TimeStampedModel):
    aluno = models.ForeignKey(Aluno)
    turma = models.ForeignKey(Turma)
    data = models.DateField()
    status = models.CharField(choices=PRESENCA_CHOICES)
```

### Mensalidade
```python
class Mensalidade(TimeStampedModel):
    aluno = models.ForeignKey(Aluno)
    valor = models.DecimalField()
    data_vencimento = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES)
```

---

## 📸 Screenshots

### Login
![Login](https://via.placeholder.com/800x600/667eea/ffffff?text=Login+Screen)

### Dashboard
![Dashboard](https://via.placeholder.com/800x600/4f46e5/ffffff?text=Dashboard)

### Cadastro de Aluno
![Cadastro](https://via.placeholder.com/800x600/10b981/ffffff?text=Cadastro+Aluno)

---

## 🤝 Contribuidores

**David Silva** - Desenvolvedor
- GitHub: [@DaviSilva70](https://github.com/DaviSilva70)
- Centro Universitário Unidombosco

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📞 Suporte

Se tiver alguma dúvida ou problema, abra uma issue no [GitHub Issues](https://github.com/DaviSilva70/Projeto_Sistema_Escolar/issues).

---

## 🙏 Agradecimentos

- [Django](https://www.djangoproject.com/) - Framework web
- [Bootstrap](https://getbootstrap.com/) - Framework CSS
- [Bootstrap Icons](https://icons.getbootstrap.com/) - Ícones
- [Google Fonts](https://fonts.google.com/) - Fonte Inter
- [Centro Universitário Unidombosco](https://www.unidombosco.edu.br/) - Instituição de ensino
