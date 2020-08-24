from django.shortcuts import render

from produto.models import Product


def lista_produtos(request):
    products = Product.objects.all().order_by('name')
    phrase = "Esta frase está sendo exibida pela página index.html de produto."
    return render(request, 'product/products.html', {'products': products})
