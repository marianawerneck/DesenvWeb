from django.shortcuts import render


def index(request):
    phrase = "Exibited phrase";
    return render(request, "index.html", {"phrase":phrase})