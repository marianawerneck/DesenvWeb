from django.urls import path

from produto import views

app_name = 'produto'

urlpatterns = [
    path('lista_produtos/', views.lista_produtos, name='lista_produtos')
]