from django.db import models
from PIL import Image


class NovoProduto(models.Model):
     novo_produto = models.CharField(max_length=100)

     def __str__(self) -> str:
          return self.novo_produto

class NovoValor(models.Model):
     novo_valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

     def __str__(self):
          return f' R${self.novo_valor}'

class Produto(models.Model):
     tipo = models.ForeignKey(NovoProduto, on_delete=models.CASCADE)
     imagem = models.ImageField(upload_to='imagens/',blank=True, null=True)
     nome_produto = models.CharField(max_length=100, blank=True, null=True)
     descricao = models.TextField(blank=True, null=True)
     valor = models.ForeignKey(NovoValor, on_delete=models.CASCADE)

     def __str__(self):
          return f"- {self.tipo} - {self.imagem} - {self.nome_produto} - {self.descricao} -  R${self.valor}"


     def save(self, *args, **kwargs):
          super().save(*args, **kwargs)

          if self.imagem:
               img = Image.open(self.imagem.path)

               # Defina as larguras e alturas desejadas
               largura_padrao = 168
               altura_padrao = 168

               # Redimensione a imagem
               img.thumbnail((largura_padrao, altura_padrao))
               img.save(self.imagem.path)
