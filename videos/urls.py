from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_videos, name='lista_videos'),
    path('cadastro/', views.cadastro_video, name='cadastro_video'),
    path('<int:pk>/', views.detalhe_video, name='detalhe_video'),
    path('<int:pk>/editar/', views.editar_video, name='editar_video'),
    path('<int:pk>/excluir/', views.excluir_video, name='excluir_video'),
]
