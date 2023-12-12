from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(NovoProduto)
class NovoProdutoADM(admin.ModelAdmin):
     list_display = ('novo_produto',)

@admin.register(NovoValor)
class NovoValorADM(admin.ModelAdmin):
     list_display = ('novo_valor',)

@admin.register(Produto)
class ProdutoADM(admin.ModelAdmin):
     list_display = ('tipo', 'nome_produto', 'descricao', 'valor',)
