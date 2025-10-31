# base/views.py
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Artigo
from django.contrib.auth.decorators import login_required
from django.db.models import Q # Importação para a busca com "OU"

@login_required # <-- Isso protege a página, exigindo login
def home(request):
    categorias = Categoria.objects.all()
    artigos_recentes = Artigo.objects.all()[:5]
    return render(request, 'base/home.html', {
        'categorias': categorias,
        'artigos_recentes': artigos_recentes
    })

@login_required
def categoria_detail(request, slug):
    # Encontra a categoria atual
    categoria = get_object_or_404(Categoria, slug=slug)
    
    # Busca as subcategorias diretas (filhas) desta categoria
    subcategorias = categoria.children.all() 
    
    # Busca os artigos que pertencem DIRETAMENTE a esta categoria
    artigos = Artigo.objects.filter(categoria=categoria)
    
    return render(request, 'base/categoria_detail.html', {
        'categoria': categoria,
        'subcategorias': subcategorias, # Passa as subcategorias para o template
        'artigos': artigos,            # Passa os artigos diretos para o template
    })

@login_required
def artigo_detail(request, slug):
    artigo = get_object_or_404(Artigo, slug=slug)
    return render(request, 'base/artigo_detail.html', {'artigo': artigo})


# --- NOVA FUNÇÃO DE BUSCA ADICIONADA AQUI ---

@login_required
def search_results(request):
    query = request.GET.get('q') # Pega o parâmetro 'q' da URL (ex: /search/?q=sip)
    results = []

    if query:
        # Busca artigos onde o 'titulo' OU o 'conteudo' contenham a palavra (sem diferenciar maiúsculas/minúsculas)
        results = Artigo.objects.filter(
            Q(titulo__icontains=query) | Q(conteudo__icontains=query)
        ).distinct()

    return render(request, 'base/search_results.html', {
        'query': query,
        'results': results,
    })