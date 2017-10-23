from django.db import models
from categories.models import Category

class Product(models.Model):
    name = models.CharField('Nome', max_length=150)
    size = models.CharField('Tamanho', max_length=30)
    description = models.TextField('Descrição', blank=True)
    acquiredValue = models.IntegerField('Valor de Frabricacao', blank=True ,default=0)
    amount = models.IntegerField('Quantidade')
    saleValue = models.IntegerField('Valor de Venda')
    category = models.ForeignKey(Category, verbose_name="Categoria")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

class FactoryItem(models.Model):
    name = models.CharField('Nome', max_length=150)
    value = models.IntegerField('Valor')
    company = models.CharField('Empresa', max_length=150, blank=True)
    salesMan = models.CharField('Vendedor', max_length=150, blank=True)
    product = models.ForeignKey(Product, verbose_name="Produto")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fabricacao de Produto'
        verbose_name_plural = 'Fabricacao de Produtos'
        ordering = ['name']
