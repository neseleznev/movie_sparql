# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('contributors', models.ManyToManyField(related_name='movies', to='web.Contributor')),
            ],
        ),
        migrations.AddField(
            model_name='contributor',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors', to='web.Genre'),
        ),
    ]