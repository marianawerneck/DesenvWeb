from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from carrinho.carrinho import Carrinho
from carrinho.forms import QuantidadeForm
from categoria.models import Category
from produto.models import Product

def lista_produtos(request, slug_da_categoria=None):
    categoria = None
    categorias = Category.objects.all().order_by('name')
    produtos = Product.objects.filter(available=True).order_by('name')
    if slug_da_categoria:
        categoria = get_object_or_404(Category, slug=slug_da_categoria)
        produtos = produtos.filter(category=categoria).order_by('name')

    carrinho = Carrinho(request)
    lista_de_forms = []
    for produto in produtos:
        qtd = carrinho.get_quantidade_total(produto.id)
        lista_de_forms.append(QuantidadeForm(initial={'quantidade': qtd, 'produto_id': produto.id}))

    return render(request, 'carrinho/lista_produtos.html', {'categorias': categorias,
                                                            'listas': zip(produtos, lista_de_forms),
                                                            'categoria': categoria})

def exibe_produto(request, id, slug_do_produto):
    produto = get_object_or_404(Product, id=id)

    return render(request, 'carrinho/exibe_produto.html', {'produto': produto})

def atualiza_carrinho(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        produto_id = form.cleaned_data['produto_id']
        quantidade = form.cleaned_data['quantidade']

        carrinho = Carrinho(request)
        if (quantidade == 0):
            carrinho.remover(produto_id)
            preco_total = 0.0
        else:
            carrinho.atualiza(produto_id, quantidade)
            preco_total = carrinho.get_preco_total(produto_id)

        qtd = carrinho.get_quantidade_carrinho()
        preco_carrinho = carrinho.get_preco_carrinho()

        print('***** id do produto = ' + produto_id +
              '  quantidade = ' + str(quantidade) +
              '  preço total do produto = ' + str(preco_total))
        print('***** qtd no carrinho = ' + str(qtd) +
              '  valor do carrinho = ' + str(preco_carrinho))

        return render(request, 'carrinho/resposta_ajax.html')
    else:
        raise ValueError('Ocorreu um erro inesperado ao adicionar um produto ao carrinho.')
























