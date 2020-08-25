from carrinho.carrinho import Carrinho


def calcula_totais_carrinho(request):
    carrinho = Carrinho(request)
    quantidade = carrinho.get_quantidade_carrinho()
    preco_carrinho = carrinho.get_preco_carrinho()
    return {
        'quantidade': quantidade,
        'preco_carrinho': preco_carrinho
    }