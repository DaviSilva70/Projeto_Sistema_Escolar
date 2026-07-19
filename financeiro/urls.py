from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mensalidades, name='lista_mensalidades'),
    path('cadastro/', views.cadastro_mensalidade, name='cadastro_mensalidade'),
    path('<int:pk>/editar/', views.editar_mensalidade, name='editar_mensalidade'),
    path('pagamento/<int:pk>/', views.registrar_pagamento, name='registrar_pagamento'),
]
