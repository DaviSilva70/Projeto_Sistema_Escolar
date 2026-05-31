from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),
    path('lancamento/', views.lancamento_notas, name='lancamento_notas'),
    path('boletim/<int:aluno_pk>/', views.boletim_aluno, name='boletim_aluno'),
]
