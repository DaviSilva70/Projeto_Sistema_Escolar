from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_comunicados, name='lista_comunicados'),
    path('cadastro/', views.cadastro_comunicado, name='cadastro_comunicado'),
    path('<int:pk>/', views.detalhe_comunicado, name='detalhe_comunicado'),
]
