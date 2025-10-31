# base/context_processors.py
from .models import Categoria

def all_categories(request):
    """
    Disponibiliza APENAS as categorias de PRIMEIRO NÍVEL (sem pai) 
    para todos os templates (usado no menu lateral).
    """
    return {
        # parent__isnull=True filtra apenas as que não têm pai
        'all_categories': Categoria.objects.filter(parent__isnull=True) 
    }