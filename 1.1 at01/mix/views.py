from django.shortcuts import render, get_object_or_404
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'mix/home.html', {'produtos': produtos})

def produto_detalhe(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'mix/produto_detalhe.html', {'produto': produto})