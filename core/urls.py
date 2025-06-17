<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from imagens.views import gerar_view  # importa direto da view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gerar_view, name='gerador'),  # rota principal chama a função gerar_view
=======
from django.urls import path
from .views import home, custom_logout

urlpatterns = [
    path('',        home,         name='home'),
    path('logout/', custom_logout, name='logout'),
>>>>>>> a01d72b9a120858c4f760b89a99cabe8b2b1b9ed
]
