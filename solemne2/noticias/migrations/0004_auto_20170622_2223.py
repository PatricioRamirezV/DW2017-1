# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 22:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_auto_20170622_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id_categoria',
        ),
        migrations.RemoveField(
            model_name='news',
            name='id_noticia',
        ),
    ]
