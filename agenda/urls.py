from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('cadastro/', views.cadastro_evento, name='cadastro_evento'),
    path('<int:pk>/editar/', views.editar_evento, name='editar_evento'),
    path('<int:pk>/excluir/', views.excluir_evento, name='excluir_evento'),
]
