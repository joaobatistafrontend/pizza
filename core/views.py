from django.shortcuts import render
from django.views.generic import View,TemplateView, ListView
from .models import *



class Index(TemplateView):
    template_name = 'inde.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        # Buscar dinamicamente os tipos de produtos existentes
        tipos_produto = NovoProduto.objects.all()
        context['tipos_produto'] = tipos_produto
# Buscar dinamicamente os produtos relacionados a todos os tipos de produtos existentes
        produtos_relacionados = {}
        for tipo in tipos_produto:
          produtos_relacionados[tipo.novo_produto] = Produto.objects.filter(tipo=tipo)

        context['produtos_relacionados'] = produtos_relacionados

       # Lista de tipos desejados
        #tipos_desejados = ['Pizza', 'Massas']

        # Filtra os produtos com base nos tipos desejados
        #produtos = Produto.objects.filter(tipo__novo_produto__in=tipos_desejados)

        return (context)
  
class Lista(ListView):
    template_name = 'list.html'
    model = Produto  # Certifique-se de substituir pelo seu modelo real

    def get_queryset(self):
        tipo_pk = self.kwargs['pk']
        return Produto.objects.filter(tipo__pk=tipo_pk)
