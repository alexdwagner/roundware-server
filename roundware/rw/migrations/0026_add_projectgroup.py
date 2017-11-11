# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-10 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rw', '0025_ui_model_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, max_length=2048)),
                ('projects', models.ManyToManyField(blank=True, to='rw.Project')),
            ],
        ),
    ]
