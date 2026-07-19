# Sistema de Gestao Escolar (SGE)

[![Django](https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.x-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

> Sistema completo para gerenciamento escolar com controle de acesso por perfil, cadastro de alunos, professores, turmas, disciplinas, notas, frequencia, financeiro, comunicados, videos educacionais e relatorios com PDF.

---

## Indice

- [Visao Geral](#visao-geral)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias](#tecnologias)
- [Instalacao](#instalacao)
- [Controle de Acesso](#controle-de-acesso)
- [Models](#models)
- [Seguranca](#seguranca)
- [Historico de Erros e Correcoes](#historico-de-erros-e-correcoes)
- [Contribuidores](#contribuidores)
- [Licenca](#licenca)

---

## Visao Geral

O **Sistema de Gestao Escolar (SGE)** e uma aplicacao web desenvolvida em Django para auxiliar na administracao de instituicoes de ensino. O sistema permite gerenciar alunos, professores, turmas, disciplinas, notas, frequencia, financeiro, comunicados e videos educacionais de forma integrada e segura.

### Autor
**David Silva** - Centro Universitario Unidombosco

---

## Funcionalidades

### Gestao de Alunos
- Cadastro completo com dados pessoais
- Upload de foto para registro
- Vinculacao com responsavel (Pai, Mae, Avo, Tio, etc.)
- Controle de status (ativo/inativo)
- Busca e filtros com paginacao
- CRUD completo com validacao de formulario
- **Gestão de Responsáveis**:
  - Cadastro simplificado diretamente no aluno
  - Tipos abrangentes (pai, mãe, avô/tio etc.)
  - Controle central por CPF e vínculo escolar

### Gestao de Professores
- Cadastro com dados profissionais
- Formacao e especialidade
- Upload de foto
- Matricula e salario

### Gestao de Turmas
- Series e niveis (Fundamental I, II, Medio)
- Turnos (Manha, Tarde, Noite)
- Capacidade e sala de aula
- Ano letivo

### Gestao de Disciplinas
- Cadastro de disciplinas
- Carga horaria
- Obrigatorias e optativas
- Edicao e exclusao

### Sistema de Notas
- Lancamento de notas por bimestre
- Tipos de avaliacao (Prova, Trabalho, Atividade, Participacao)
- Boletim escolar por aluno

### Controle de Frequencia
- Chamada digital por turma
- Registro de presenca, ausencia, justificado e atrasado
- Historico de frequencia por aluno
- Protecao contra registros duplicados (unique_together)

### Gestao Financeira
- Cadastro de mensalidades com valor e desconto
- Registro de pagamentos
- Status (Pago, Pendente, Atrasado, Isento)
- Controle de vencimento

### Comunicados
- Avisos gerais e por turma
- Prioridade (Baixa, Media, Alta)
- Data de validade
- **Marcacao como lido** por cada usuario

### Agenda
- Calendario de eventos
- Eventos por turma
- Cores personalizadas
- Edicao e exclusao

### Biblioteca de Videos
- Cadastro de videos educacionais (YouTube/Vimeo)
- Categorias: Aula, Tutorial, Palestra, Documentario, Animacao
- Vinculacao com disciplina e turmas
- Player incorporado (iframe)
- ### Seção de Vídeos e Disciplinas
  - Integração: todos associados à disciplina e turma
  - Upload fácil: momentos didáticos
  - Restrições (iframe seguro)
  - Métodos formutils-disciplina-view associados (`POST`) security.py
- Controle de ordem de exibicao

### Relatorios
- Dashboard administrativo com estatisticas gerais
- Relatorio de desempenho academico com filtros
- Relatorio de frequencia por turma
- **Exportacao em PDF** com reportlab (Desempenho e Frequencia)
- Ranking de alunos por media

---

## Estrutura do Projeto

```
Projeto_Web_Escola_Django/
├── config/                    # Configuracoes do projeto
│   ├── settings.py            # Settings com .env (python-decouple)
│   ├── urls.py
│   └── wsgi.py
│
├── core/                      # Modelos base e utilitarios
│   ├── models.py              # TimeStampedModel, AtivoManager
│   └── utils/
│       └── permissoes.py      # @perfil_requerido, PerfilMixin
│
├── accounts/                  # Usuarios e autenticacao
│   ├── models.py              # User (AbstractUser customizado)
│   ├── views.py               # Login, Logout, Dashboard
│   └── admin.py
│
├── alunos/                    # Gestao de alunos
│   ├── models.py              # Aluno, Responsavel
│   ├── views.py               # CRUD Aluno + CRUD Responsavel
│   ├── forms.py               # ResponsavelForm, AlunoCadastroForm, AlunoEditarForm
│   └── urls.py
│
├── professores/               # Gestao de professores
│   ├── models.py              # Professor
│   ├── views.py               # CRUD Professor
│   ├── forms.py               # ProfessorCadastroForm, ProfessorEditarForm
│   └── urls.py
│
├── turmas/                    # Gestao de turmas
│   ├── models.py              # Turma, TurmaAluno
│   ├── views.py               # CRUD Turma
│   ├── forms.py               # TurmaForm
│   └── urls.py
│
├── disciplinas/               # Gestao de disciplinas
│   ├── models.py              # Disciplina, DisciplinaTurma
│   ├── views.py               # CRUD Disciplina
│   ├── forms.py               # DisciplinaForm
│   └── urls.py
│
├── notas/                     # Notas e boletins
│   ├── models.py              # Nota
│   ├── views.py               # Lancamento, Lista, Boletim
│   ├── forms.py               # NotaForm
│   └── urls.py
│
├── frequencia/                # Controle de frequencia
│   ├── models.py              # Frequencia
│   ├── views.py               # Chamada, Historico
│   ├── forms.py               # FrequenciaForm
│   └── urls.py
│
├── financeiro/                # Gestao financeira
│   ├── models.py              # Mensalidade
│   ├── views.py               # CRUD Mensalidade + Pagamento
│   ├── forms.py               # MensalidadeForm
│   └── urls.py
│
├── comunicados/               # Comunicados
│   ├── models.py              # Comunicado
│   ├── views.py               # CRUD + Marcar como lido
│   ├── forms.py               # ComunicadoForm
│   └── urls.py
│
├── agenda/                    # Agenda e eventos
│   ├── models.py              # Evento
│   ├── views.py               # CRUD Evento
│   ├── forms.py               # EventoForm
│   └── urls.py
│
├── videos/                    # Biblioteca de videos
│   ├── models.py              # Video (YouTube/Vimeo embed)
│   ├── views.py               # CRUD Video
│   ├── forms.py               # VideoForm
│   ├── admin.py
│   └── urls.py
│
├── relatorios/                # Relatorios e PDFs
│   ├── views.py               # Dashboard, Desempenho, Frequencia, PDFs
│   └── urls.py
│
├── templates/                 # Templates HTML (~50 arquivos)
│   ├── base.html              # Layout com sidebar responsiva
│   ├── login.html             # Tela de login
│   ├── dashboard.html         # Painel principal
│   ├── cadastro_perfil.html   # Escolha de perfil
│   ├── 403.html               # Acesso negado
│   ├── alunos/                # Templates de alunos + responsaveis
│   ├── professores/           # Templates de professores
│   ├── turmas/                # Templates de turmas
│   ├── disciplinas/           # Templates de disciplinas
│   ├── notas/                 # Templates de notas
│   ├── frequencia/            # Templates de frequencia
│   ├── financeiro/            # Templates financeiros
│   ├── comunicados/           # Templates de comunicados
│   ├── relatorios/            # Templates de relatorios
│   ├── agenda/                # Templates de agenda
│   └── videos/                # Templates de videos
│
├── static/                    # Arquivos estaticos
│   ├── css/custom.css         # CSS moderno (18KB)
│   ├── js/custom.js           # JavaScript customizado
│   └── img/
│
├── media/                     # Arquivos de midia
│
├── .env                       # Variaveis de ambiente (nao versionado)
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Tecnologias

| Camada | Tecnologia |
|--------|------------|
| **Backend** | Django 5.x / Python 3.12+ |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Banco de Dados** | MySQL 8.x |
| **Autenticacao** | Django Auth + Custom User Model |
| **Validacao** | Django Forms (server-side) |
| **Relatorios PDF** | ReportLab |
| **Variaveis de Ambiente** | python-decouple |
| **Administrativo** | Django Admin customizado |
| **Icones** | Bootstrap Icons |
| **Fonte** | Google Fonts (Inter) |

---

## Instalacao

### Pre-requisitos
- Python 3.12+
- MySQL 8.x
- pip

### 1. Clone o repositorio
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

### 3. Instale as dependencias
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
mysql -u root -p
CREATE DATABASE bd_escola CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### 5. Configure as variaveis de ambiente
Edite o arquivo `.env` na raiz do projeto:
```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
DB_NAME=bd_escola
DB_USER=root
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
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

## Controle de Acesso

### Perfis de Usuario

| Perfil | Descricao | Permissoes |
|--------|-----------|------------|
| `admin` | Administrador | Acesso total ao sistema |
| `diretor` | Diretor | Acesso administrativo completo |
| `professor` | Professor | Notas, frequencia, comunicados, agenda, videos |
| `aluno` | Aluno | Suas notas, frequencia, comunicados, videos |
| `responsavel` | Responsavel | Dados dos filhos |
| `funcionario` | Funcionario | Acesso limitado |

### Mapeamento de Permissoes por Pagina

| Pagina | Admin | Diretor | Professor | Aluno |
|--------|-------|---------|-----------|-------|
| Dashboard | ✅ | ✅ | ✅ | ✅ |
| Alunos | ✅ | ✅ | ❌ | ❌ |
| Responsaveis | ✅ | ✅ | ❌ | ❌ |
| Professores | ✅ | ✅ | ❌ | ❌ |
| Turmas | ✅ | ✅ | ❌ | ❌ |
| Disciplinas | ✅ | ✅ | ❌ | ❌ |
| Notas | ✅ | ✅ | ✅ | ✅ (proprias) |
| Frequencia | ✅ | ✅ | ✅ | ✅ (propria) |
| Agenda | ✅ | ✅ | ✅ | ❌ |
| Financeiro | ✅ | ✅ | ❌ | ❌ |
| Comunicados | ✅ | ✅ | ✅ | ✅ |
| Videos | ✅ | ✅ | ✅ | ✅ |
| Relatorios | ✅ | ✅ | ❌ | ❌ |

### Decorator de Permissao
```python
from core.utils.permissoes import perfil_requerido

# Apenas admin e diretor
@perfil_requerido('admin', 'diretor')
def minha_view(request):
    ...

# Admin, diretor e professor
@perfil_requerido('admin', 'diretor', 'professor')
def view_academica(request):
    ...
```

### Para que serve
- `@perfil_requerido` — verifica o campo `tipo` do usuario logado
- `@login_required` — exige autenticacao (qualquer perfil)
- Todos os endpoints de escrita usam `@perfil_requerido`
- Todas as views de leitura usam `@login_required` ou `@perfil_requerido`

---

## Models

### User (Custom)
```python
class User(AbstractUser):
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='usuarios/')
    ativo = models.BooleanField(default=True)
```

### Responsavel
```python
class Responsavel(TimeStampedModel):
    tipo = models.CharField(choices=TIPO_CHOICES)  # mae, pai, avo, tio, etc.
    nome_completo = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    profissao = models.CharField(max_length=100)
```

### Aluno
```python
class Aluno(TimeStampedModel):
    user = models.OneToOneField(User)
    ra = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    responsavel = models.ForeignKey(Responsavel)
```

### Professor
```python
class Professor(TimeStampedModel):
    user = models.OneToOneField(User)
    matricula = models.CharField(max_length=20, unique=True)
    formacao = models.CharField(max_length=100)
    data_admissao = models.DateField()
    salario = models.DecimalField()
```

### Video
```python
class Video(TimeStampedModel):
    titulo = models.CharField(max_length=200)
    url = models.URLField()  # YouTube ou Vimeo
    categoria = models.CharField(choices=CATEGORIA_CHOICES)
    disciplina = models.ForeignKey(Disciplina, null=True)
    turmas = models.ManyToManyField(Turma)
    autor = models.ForeignKey(User)
```

---

## Seguranca

### Medidas Implementadas

1. **Controle de acesso por perfil** — Todas as views de escrita usam `@perfil_requerido`
2. **Validacao server-side** — Django Forms com validacao de CPF, data, valores, URL
3. **Protecao contra IntegridyError** — Todas as views de criacao tratam uniques constraint
4. **CSRF Protection** — Middleware ativo em todas as paginas
5. **Secret Key via .env** — Chave secreta em variavel de ambiente, nao hardcoded
6. **DEBUG via .env** — Controle de debug por variavel de ambiente
7. **Paginacao** — Todas as listagens paginadas (15 itens/pagina)
8. **Tratamento de 403** — Pagina customizada de acesso negado
9. **Sidebar condicional** — Itens de menu filtrados por perfil no template
10. **Validacao de URL** — VideoForm aceita apenas YouTube/Vimeo

### Arquivo .env (nao versionado)
```env
SECRET_KEY=chave-secreta
DEBUG=True
DB_NAME=bd_escola
DB_USER=root
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=3306
```

---

## Endpoints Principais

| URL | Descricao | Permissao |
|-----|-----------|-----------|
| `/login/` | Login | Publico |
| `/cadastro/` | Escolha de perfil | Publico |
| `/cadastro/alunos/cadastro-publico/` | Cadastro de aluno | Publico |
| `/cadastro/professores/cadastro-publico/` | Cadastro de professor | Publico |
| `/` | Dashboard | Logado |
---

## Historico de Erros e Correcoes

> Registro de bugs encontrados e suas solucoes durante o desenvolvimento.

### 1. Banco de dados: MySQL nao conectava

**Erro:** `django.db.utils.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: NO)")`

**Causa:** O arquivo `.env` tinha `DB_ENGINE=sqlite3` mas a variavel de ambiente do terminal (VS Code) tambem definia `DB_ENGINE=sqlite3`. O `python-decouple` prioriza variaveis de ambiente do sistema sobre o `.env`, entao o Django continuava usando SQLite mesmo apos alterar o `.env`.

**Correcao em `config/settings.py`:**
```python
import os
from decouple import config, Csv

# Forca precedencia do .env: remove variaveis de ambiente stale do shell
for _var in ('DB_ENGINE', 'DB_NAME', 'DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT'):
    os.environ.pop(_var, None)
```

**Arquivos alterados:** `config/settings.py`

---

### 2. Venv apontava para Python inexistente (Anaconda)

**Erro:** `did not find executable at 'C:\Anaconda_3_13_Python\python.exe'`

**Causa:** O `venv` foi criado com Anaconda 3.13 que nao existe mais na maquina. O `pyvenv.cfg` apontava para o caminho morto.

**Correcao:** Remover o venv antigo e recriar com o Python disponivel:
```bash
rm -rf venv
"C:/Python 3.14.5/python.exe" -m venv venv
pip install -r requirements.txt
```

**Arquivos alterados:** `venv/`, `requirements.txt` (adicionado `mysqlclient>=2.2`)

---

### 3. Cadastro de Aluno/Professor nunca funcionava (campos incompativeis)

**Erro:** Formulario aceita dados no navegador mas nada e gravado no banco. `is_valid()` retorna `False` silenciosamente.

**Causa:** Os nomes dos campos nos templates HTML nao batiam com os nomes nos forms Django:

| Template enviava | Form esperava |
|------------------|---------------|
| `tipo_responsavel` | `responsavel_tipo` |
| `nome_responsavel` | `responsavel_nome` |
| `cpf_responsavel` | `responsavel_cpf` |
| `telefone_responsavel` | `responsavel_telefone` |
| `email_responsavel` | `responsavel_email` |
| `endereco_responsavel` | `responsavel_endereco` |
| `profissao_responsavel` | `responsavel_profissao` |
| `endereco` | `endereco_aluno` |

Todos os campos de responsavel eram obrigatorios e sempre chegavam vazios -> `is_valid()` retornava `False`.

**Correcao:** Renomeei todos os campos do `AlunoCadastroForm` e `AlunoEditarForm` para bater com os templates:
```python
# Antes (errado)
responsavel_tipo = forms.CharField(...)
endereco_aluno = forms.CharField(...)

# Depois (correto)
tipo_responsavel = forms.CharField(...)
endereco = forms.CharField(...)
```

Atualizei as views `cadastro_aluno`, `cadastro_aluno_publico` e `editar_aluno` para usar os novos nomes.

**Arquivos alterados:** `alunos/forms.py`, `alunos/views.py`

---

### 4. Campo parentesco usava TextInput em vez de Select

**Erro:** O campo `responsavel_tipo` era `forms.TextInput` (campo de texto livre), mas o template renderizava um `<select>` com valores fixos (mae, pai, avo, etc).

**Correcao:** Trocado para `forms.Select` com as choices do modelo:
```python
tipo_responsavel = forms.CharField(label='Parentesco', widget=forms.Select(
    attrs=WIDGET_ATTRS,
    choices=[('', 'Selecione o parentesco')] + Responsavel.TIPO_CHOICES
))
```

**Arquivos alterados:** `alunos/forms.py`

---

### 5. Datas nao aceitavam formato brasileiro (DD/MM/YYYY)

**Erro:** Usuário brasileiro digita `19/07/2026` mas o form rejeita com "Enter a valid date."

**Causa:** `DateField` com `DateInput(attrs={'type': 'date'})` so aceita formato ISO `YYYY-MM-DD`.

**Correcao:** Adicionado `input_formats` para aceitar ambos os formatos e trocado o widget para texto com placeholder:
```python
data_nascimento = forms.DateField(
    label='Data de Nascimento',
    input_formats=['%d/%m/%Y', '%Y-%m-%d'],
    widget=forms.DateInput(attrs={**WIDGET_ATTRS, 'placeholder': 'dd/mm/aaaa', 'type': 'text'})
)
```

**Arquivos alterados:** `alunos/forms.py`, `professores/forms.py`

---

### 6. Template professor publico sem campo salario

**Erro:** Cadastro publico de professor rejeita o formulario com erro "This field is required" no salario.

**Causa:** O template `templates/professores/cadastro_publico.html` nao renderizava o campo `salario`, mas o `ProfessorCadastroForm` o exige.

**Correcao:** Adicionado o campo no template:
```html
<div class="col-md-6">
    <label class="form-label">Salario (R$) *</label>
    <input type="number" name="salario" class="form-control" step="0.01" placeholder="0.00" required>
</div>
```

**Arquivos alterados:** `templates/professores/cadastro_publico.html`

---

### 7. Senha inutilizavel em todos os cadastros (CRITICAL)

**Erro:** Usuario se cadastra mas nao consegue logar. A senha gerada comeca com `!` (hash inutilizavel Django).

**Causa:** As 4 views de cadastro chamavam `User.objects.create_user()` **sem passar o parametro `password`**. O Django 6.0 cria o usuario com `set_unusable_password()`, gerando um hash que comeca com `!`. O usuario literalmente nunca consegue autenticar.

```python
# ERRADO - sem password
user = User.objects.create_user(
    username=cd['ra'],
    first_name=cd['first_name'],
    # ... sem password!
)

# CORRETO - com password gerado
senha = _gerar_senha()  # ex: '!qS6wf!1V1w6'
user = User.objects.create_user(
    username=cd['ra'],
    first_name=cd['first_name'],
    password=senha,  # <-- ESSENCIAL
    # ...
)
```

**Correcao:** Funcao `_gerar_senha()` gera senha segura com `secrets` + `string`. A senha e exibida ao usuario apos o cadastro:
```python
import secrets, string

def _gerar_senha(length=12):
    while True:
        pw = ''.join(secrets.choice(string.ascii_letters + string.digits + '!@#$%&*') for _ in range(length))
        if (any(c.isupper() for c in pw) and any(c.islower() for c in pw)
                and any(c.isdigit() for c in pw) and any(c in '!@#$%&*' for c in pw)):
            return pw
```

Mensagem de sucesso agora inclui login e senha:
```python
messages.success(request,
    f'Conta criada com sucesso! '
    f'Seu login: <strong>{cd["ra"]}</strong> '
    f'| Senha: <strong>{senha}</strong>. '
    f'Faça login para acessar o sistema.')
```

**Arquivos alterados:** `alunos/views.py`, `professores/views.py`

> **Nota:** `User.objects.make_random_password()` foi removido no Django 6.0. Use `secrets` diretamente.

---

### 8. Template login nao exibia mensagens

**Erro:** Apos cadastro, o usuario e redirecionado para `/login/` mas nunca ve a mensagem com login/senha.

**Causa:** O template `login.html` nao tinha bloco de rendering de mensagens `{% for message in messages %}`.

**Correcao:** Adicionado bloco de mensagens ao `login.html`:
```html
{% if messages %}
{% for message in messages %}
<div class="alert alert-success" style="border-radius: 10px; font-size: 0.85rem;">
    <span>{{ message|safe }}</span>
</div>
{% endfor %}
{% endif %}
```

Tambem adicionado Bootstrap JS para o botao de fechar alert funcionar.

**Arquivos alterados:** `templates/login.html`

---

### 9. Mensagens com HTML nao renderizavam `<strong>`

**Erro:** As tags `<strong>` na mensagem de cadastro apareciam como texto literal: `Login: <strong>RA2026099</strong>`.

**Causa:** Os templates usavam `{{ message }}` que escapa HTML por seguranca.

**Correcao:** Trocado para `{{ message|safe }}` em todos os templates que exibem mensagens:
- `templates/base.html`
- `templates/login.html`
- `templates/alunos/cadastro_publico.html`
- `templates/professores/cadastro_publico.html`

> **Nota:** So use `|safe` em mensagens que voce mesmo gera no backend. Nunca em input do usuario.

---

### 10. `make_random_password()` nao existe no Django 6.0

**Erro:** `AttributeError: 'UserManager' object has no attribute 'make_random_password'`

**Causa:** O metodo `make_random_password()` foi removido do `UserManager` no Django 6.0.

**Correcao:** Implementada funcao propria com `secrets` (.Cryptography-grade`):
```python
import secrets, string

def _gerar_senha(length=12):
    while True:
        pw = ''.join(secrets.choice(string.ascii_letters + string.digits + '!@#$%&*') for _ in range(length))
        if (any(c.isupper() for c in pw) and any(c.islower() for c in pw)
                and any(c.isdigit() for c in pw) and any(c in '!@#$%&*' for c in pw)):
            return pw
```

Garante: 1 maiuscula + 1 minuscula + 1 digito + 1 especial, minimo 12 caracteres.

---

### Resumo dos arquivos alterados

| Arquivo | Correcoes |
|---------|-----------|
| `config/settings.py` | Pop env vars para precedencia do `.env` |
| `requirements.txt` | Adicionado `mysqlclient>=2.2` |
| `alunos/forms.py` | Nomes dos campos, Select widget, datas BR |
| `alunos/views.py` | Referencias cleaned_data, geracao de senha |
| `professores/forms.py` | Datas BR (Cadastro + Edicao) |
| `professores/views.py` | Geracao de senha |
| `templates/login.html` | Bloco de mensagens + Bootstrap JS |
| `templates/base.html` | `{{ message\|safe }}` |
| `templates/alunos/cadastro_publico.html` | `{{ message\|safe }}` |
| `templates/professores/cadastro_publico.html` | Campo salario + `{{ message\|safe }}` |

| `/alunos/` | Lista de alunos | Admin/Diretor |
| `/alunos/responsaveis/` | Lista de responsaveis | Admin/Diretor |
| `/professores/` | Lista de professores | Admin/Diretor |
| `/turmas/` | Lista de turmas | Admin/Diretor |
| `/disciplinas/` | Lista de disciplinas | Admin/Diretor |
| `/notas/` | Lista de notas | Admin/Diretor/Professor |
| `/notas/lancamento/` | Lancar notas | Admin/Diretor/Professor |
| `/frequencia/chamada/` | Registrar chamada | Admin/Diretor/Professor |
| `/financeiro/` | Lista de mensalidades | Admin/Diretor |
| `/financeiro/cadastro/` | Cadastrar mensalidade | Admin/Diretor |
| `/comunicados/` | Lista de comunicados | Logado |
| `/comunicados/<pk>/lido/` | Marcar como lido | Logado |
| `/agenda/` | Lista de eventos | Logado |
| `/videos/` | Biblioteca de videos | Logado |
| `/videos/cadastro/` | Cadastrar video | Admin/Diretor/Professor |
| `/relatorios/` | Dashboard relatorios | Logado |
| `/relatorios/desempenho/` | Relatorio desempenho | Admin/Diretor |
| `/relatorios/desempenho/pdf/` | PDF desempenho | Admin/Diretor |
| `/relatorios/frequencia/` | Relatorio frequencia | Admin/Diretor |
| `/relatorios/frequencia/pdf/` | PDF frequencia | Admin/Diretor |

---

## Contribuidores

**David Silva** - Desenvolvedor
- GitHub: [@DaviSilva70](https://github.com/DaviSilva70)
- Centro Universitario Unidombosco

---

## Licenca

Este projeto esta sob a licenca MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Agradecimentos

- [Django](https://www.djangoproject.com/) - Framework web
- [Bootstrap](https://getbootstrap.com/) - Framework CSS
- [Bootstrap Icons](https://icons.getbootstrap.com/) - Icones
- [Google Fonts](https://fonts.google.com/) - Fonte Inter
- [ReportLab](https://www.reportlab.com/) - Geracao de PDFs
- [python-decouple](https://github.com/HBNetwork/python-decouple) - Variaveis de ambiente
- [Centro Universitario Unidombosco](https://www.unidombosco.edu.br/) - Instituicao de ensino
