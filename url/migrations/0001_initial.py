# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-30 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('short_id', models.SlugField(max_length=6, primary_key=True, serialize=False)),
                ('httpurl', models.URLField()),
            ],
        ),
    ]
