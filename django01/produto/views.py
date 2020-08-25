from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from produto.models import Product
from produto.forms.productForm import ProductForm


@user_passes_test(lambda u: u.is_staff)
def lista_produtos(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'product/products.html', {'products': products})


@user_passes_test(lambda u: u.is_staff)
def cadastra_produto(request):

    if request.POST:
        produto_id = request.session.get('produto_id')
        print('produto_id na sessão = ' + str(produto_id))
        if produto_id:
            produto = get_object_or_404(Product, pk=produto_id)
            produto_form = ProductForm(request.POST, request.FILES, instance=produto)
        else:
            produto_form = ProductForm(request.POST, request.FILES)

        if produto_form.is_valid():
            produto = produto_form.save(commit=False)
            produto.slug = slugify(produto.name)
            produto.save()
            if produto_id:
                messages.add_message(request, messages.INFO, 'Produto alterado com sucesso!')
                del request.session['produto_id']
            else:
                messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso!')

            return redirect('produto:exibe_produto', id=produto.id)
    else:
        try:
            del request.session['produto_id']
        except KeyError:
            pass
        produto_form = ProductForm()

    return render(request, 'product/cadastra_produto.html', {'form': produto_form})

@user_passes_test(lambda u: u.is_staff)
def exibe_produto(request, id):
    produto = get_object_or_404(Product, pk=id)
    request.session['produto_id_del'] = id
    return render(request, 'product/exibe_produto.html', {'product': produto})

@user_passes_test(lambda u: u.is_staff)
def edita_produto(request, id):
    produto = get_object_or_404(Product, pk=id)
    produto_form = ProductForm(instance=produto)
    request.session['produto_id'] = id
    return render(request, 'product/cadastra_produto.html', {'form': produto_form})

@user_passes_test(lambda u: u.is_staff)
def remove_produto(request):
    produto_id = request.session.get('produto_id_del')
    produto = get_object_or_404(Product, id=produto_id)
    produto.imagem.delete()
    produto.delete()
    del request.session['produto_id_del']
    messages.add_message(request, messages.INFO, 'Produto removido com sucesso.')
    return render(request, 'product/exibe_produto.html', {'product': produto})