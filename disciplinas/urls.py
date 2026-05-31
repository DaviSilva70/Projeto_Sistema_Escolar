from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_disciplinas, name='lista_disciplinas'),
    path('cadastro/', views.cadastro_disciplina, name='cadastro_disciplina'),
    path('<int:pk>/', views.detalhe_disciplina, name='detalhe_disciplina'),
]
