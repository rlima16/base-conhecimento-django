# Em flypabx_kb/base/urls.py

from django.urls import path
from . import views # Importa o views.py da mesma pasta

urlpatterns = [
    # A raiz ('') vai usar a view 'home'
    path('', views.home, name='home'),
    
    # Suas outras URLs que já funcionavam
    path('categoria/<slug:slug>/', views.categoria_detail, name='categoria_detail'),
    path('artigo/<slug:slug>/', views.artigo_detail, name='artigo_detail'),
    path('search/', views.search_results, name='search_results'),
]