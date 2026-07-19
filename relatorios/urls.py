from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_relatorios, name='dashboard_relatorios'),
    path('desempenho/', views.relatorio_desempenho, name='relatorio_desempenho'),
    path('desempenho/pdf/', views.relatorio_desempenho_pdf, name='relatorio_desempenho_pdf'),
    path('frequencia/', views.relatorio_frequencia, name='relatorio_frequencia'),
    path('frequencia/pdf/', views.relatorio_frequencia_pdf, name='relatorio_frequencia_pdf'),
]
