# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 05:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='id_titulo',
            new_name='id_noticia',
        ),
    ]
