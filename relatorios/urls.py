from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_relatorios, name='dashboard_relatorios'),
    path('desempenho/', views.relatorio_desempenho, name='relatorio_desempenho'),
    path('frequencia/', views.relatorio_frequencia, name='relatorio_frequencia'),
]
