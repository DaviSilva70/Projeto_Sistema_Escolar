from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_professores, name='lista_professores'),
    path('cadastro/', views.cadastro_professor, name='cadastro_professor'),
    path('cadastro-publico/', views.cadastro_professor_publico, name='cadastro_professor_publico'),
    path('<int:pk>/', views.detalhe_professor, name='detalhe_professor'),
    path('<int:pk>/editar/', views.editar_professor, name='editar_professor'),
]
