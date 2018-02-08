from django.db import models

class Category(models.Model):
    name = models.CharField('Nome', max_length=30)
    description = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name
