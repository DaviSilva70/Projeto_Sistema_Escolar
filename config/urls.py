from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import LoginView, logout_view, DashboardView
from django.shortcuts import render

def cadastro_perfil(request):
    """Página de escolha de perfil para cadastro"""
    return render(request, 'cadastro_perfil.html')

urlpatterns = [
    path("admin/", admin.site.urls),

    # Autenticação
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    # Cadastro público
    path('cadastro/', cadastro_perfil, name='cadastro_perfil'),

    # Dashboard
    path('', DashboardView.as_view(), name='dashboard'),

    # Apps
    path('alunos/', include('alunos.urls')),
    path('professores/', include('professores.urls')),
    path('turmas/', include('turmas.urls')),
    path('disciplinas/', include('disciplinas.urls')),
    path('notas/', include('notas.urls')),
    path('frequencia/', include('frequencia.urls')),
    path('financeiro/', include('financeiro.urls')),
    path('comunicados/', include('comunicados.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('agenda/', include('agenda.urls')),
]

# Servir arquivos estáticos e de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
