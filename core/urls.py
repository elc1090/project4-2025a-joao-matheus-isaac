from django.contrib import admin
from django.urls import path
from imagens.views import gerar_view  # importa direto da view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gerar_view, name='gerador'),  # rota principal chama a função gerar_view
]
