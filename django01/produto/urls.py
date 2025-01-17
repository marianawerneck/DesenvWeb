from django.urls import path

from produto import views

app_name = 'produto'

urlpatterns = [
    path('lista_produtos/', views.lista_produtos, name='lista_produtos'),
    path('cadastra_produto/', views.cadastra_produto, name='cadastra_produto'),
    path('exibe_produto/<int:id>/', views.exibe_produto, name='exibe_produto'),
    path('edita_produto/<int:id>/', views.edita_produto, name='edita_produto'),
    path('remove_produto/', views.remove_produto, name='remove_produto')
]