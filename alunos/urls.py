from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('cadastro/', views.cadastro_aluno, name='cadastro_aluno'),
    path('cadastro-publico/', views.cadastro_aluno_publico, name='cadastro_aluno_publico'),
    path('<int:pk>/', views.detalhe_aluno, name='detalhe_aluno'),
    path('<int:pk>/editar/', views.editar_aluno, name='editar_aluno'),
]
