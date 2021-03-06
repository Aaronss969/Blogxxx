# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=140)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('cuerpo', models.TextField()),
                ('slug', models.SlugField(max_length=249, unique_for_date='publicado')),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('estatus', models.CharField(choices=[('borrador', 'Borrador'), ('actualizado', 'Actualizado')], default='borrador', max_length=10)),
            ],
        ),
    ]
