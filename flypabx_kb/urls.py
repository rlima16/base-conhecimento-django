# Em flypabx_kb/flypabx_kb/urls.py

from django.contrib import admin
from django.urls import path, include # Garanta que 'include' está aqui

urlpatterns = [
    # 1. Rota do Admin (você já tem)
    path('admin/', admin.site.urls),
    
    # 2. Rotas de Autenticação (ISSO CORRIGE O 'NoReverseMatch')
    # Adiciona as URLs 'login', 'logout', 'password_reset', etc.
    path('accounts/', include('django.contrib.auth.urls')),
    
    # 3. Rota Principal (ISSO CORRIGE O 'Not Found' DO RENDER)
    # Envia todo o tráfego da raiz ('') para o seu app 'base'
    path('', include('base.urls')),
]