from django.shortcuts import render, get_object_or_404
from categoria.models import Category
from produto.models import Product

def lista_produtos(request, slug_da_categoria=None):
    categoria = None
    categorias = Category.objects.all().order_by('name')
    produtos = Product.objects.filter(available=True).order_by('name')
    if slug_da_categoria:
        categoria = get_object_or_404(Category, slug=slug_da_categoria)
        produtos = produtos.filter(category=categoria).order_by('name')

    return render(request, 'carrinho/lista_produtos.html', {'categorias': categorias,
                                                            'produtos': produtos,
                                                            'categoria': categoria})


def exibe_produto(request, id, slug_do_produto):
    produto = get_object_or_404(Product, id=id)

    return render(request, 'carrinho/exibe_produto.html', {'produto': produto})
