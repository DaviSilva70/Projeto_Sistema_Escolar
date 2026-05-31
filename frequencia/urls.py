from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_frequencia, name='lista_frequencia'),
    path('chamada/', views.chamada, name='chamada'),
    path('historico/<int:aluno_pk>/', views.historico_frequencia, name='historico_frequencia'),
]
