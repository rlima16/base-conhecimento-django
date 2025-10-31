# base/admin.py
from django.contrib import admin
from .models import Categoria, Artigo

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # Mostra o nome (com hierarquia), slug e o pai direto
    list_display = ('__str__', 'slug', 'parent') 
    # Adiciona um filtro pela categoria pai
    list_filter = ('parent',) 
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}
    # Melhora a performance ao buscar o 'parent'
    raw_id_fields = ('parent',) 

# ... A classe ArtigoAdmin continua igual ...
@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_atualizacao')
    list_filter = ('categoria', 'data_atualizacao')
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}