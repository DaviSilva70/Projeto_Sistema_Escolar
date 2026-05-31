from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mensalidades, name='lista_mensalidades'),
    path('pagamento/<int:pk>/', views.registrar_pagamento, name='registrar_pagamento'),
]
