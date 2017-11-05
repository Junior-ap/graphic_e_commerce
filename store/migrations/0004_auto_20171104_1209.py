# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-04 15:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20171026_1436'),
        ('store', '0003_auto_20171104_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amounts', models.IntegerField(verbose_name='Quantidade')),
                ('value', models.IntegerField(verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Carrinho',
                'verbose_name_plural': 'Carrinhos',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, verbose_name='Cliente')),
                ('valueTotal', models.IntegerField(verbose_name='Valor Total')),
                ('status', models.IntegerField(choices=[(0, 'comprando'), (1, 'finalizada'), (2, 'preparando'), (3, 'entrege')], default=0, verbose_name='Status')),
                ('dateStart', models.DateTimeField(auto_now_add=True, verbose_name='Data Compra')),
                ('dateEnd', models.DateTimeField(verbose_name='Data Entrega')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Ordem',
                'verbose_name_plural': 'Ordens',
                'ordering': ['dateStart'],
            },
        ),
        migrations.RemoveField(
            model_name='ordersalesman',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrderSalesman',
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order', verbose_name='Ordem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Produto'),
        ),
    ]
