# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo',
            name='slug',
            field=models.SlugField(max_length=100, null=True, verbose_name='Nome'),
        ),
    ]
