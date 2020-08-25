
from django.urls import path

from carrinho import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('<slug:slug_da_categoria>/', views.lista_produtos, name='lista_produtos_por_categoria'),
    path('<int:id>/<slug:slug_do_produto>/', views.exibe_produto, name='exibe_produto')
]