# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-15 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_imgdefault'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imgDefault',
            field=models.CharField(max_length=350, verbose_name='Imagem Padrão'),
        ),
    ]
