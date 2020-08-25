from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from autenticacao.forms import UsuarioFormCustomizado
from projeto import settings


def registra_usuario(request):
    if request.method == 'POST':
        form = UsuarioFormCustomizado(request.POST)

        if form.is_valid():
            novo_usuario = form.save()
            request.session['usuario_id'] = novo_usuario.id


            return redirect('autenticacao:exibe_usuario')
    else:
        form = UsuarioFormCustomizado()

    return render(request, 'autenticacao/registra_usuario.html', {'form': form})

def exibe_usuario(request):
    usuario = get_object_or_404(User, pk=request.session['usuario_id'])
    return render(request, 'autenticacao/exibe_usuario.html', {'usuario': usuario})
