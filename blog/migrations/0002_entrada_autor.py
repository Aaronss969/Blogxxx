# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='autor',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
