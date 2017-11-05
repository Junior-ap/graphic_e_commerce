from django.db import models
from accounts.models import User
from products.models import Product

class Order(models.Model):
    SHOPPING = 0
    FINISHED = 1
    PREPARING = 2
    DELIVERED = 3
    STATUS= (
        (SHOPPING, 'comprando'),
        (FINISHED, 'finalizada'),
        (PREPARING, 'preparando'),
        (DELIVERED, 'entrege'),
    )
    name = models.CharField('Cliente', max_length= 150, null=True)
    valueTotal = models.FloatField('Valor Total', null=True, default=0)
    status = models.IntegerField('Status', choices=STATUS, default=SHOPPING)
    dateStart = models.DateTimeField('Data Compra', auto_now=True)
    dateEnd = models.DateTimeField('Data Entrega', null=True)
    user = models.ForeignKey(User, verbose_name="Usuario")

    class Meta:
        verbose_name = 'Ordem'
        verbose_name_plural = 'Ordens'
        ordering = ['dateStart']


class Cart(models.Model):
    amounts = models.IntegerField('Quantidade')
    value = models.FloatField('Valor', default=0)
    product = models.ForeignKey(Product, verbose_name="Produto")
    order = models.ForeignKey(Order, verbose_name="Ordem")

    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'
        ordering = ['order']
