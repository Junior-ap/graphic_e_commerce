from django.db import models
from accounts.models import User

class Address(models.Model):
    cep = models.IntegerField('Cep')
    street = models.CharField('Rua', max_length=200)
    number = models.CharField('Número', max_length=30)
    neighborhood = models.CharField('Bairro', max_length=100)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=3)
    user = models.ForeignKey(User, verbose_name="Usuario", null=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['city']
