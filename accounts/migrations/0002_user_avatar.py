# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-12 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='https://res.cloudinary.com/dmpzwgmyh/image/upload/v1510449413/user_defalt_bto43s.png', max_length=350, verbose_name='Foto'),
        ),
    ]
