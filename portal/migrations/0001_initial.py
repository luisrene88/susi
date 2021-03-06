# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-19 00:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img/articulos', verbose_name='Audio (opcional)')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Articulos')),
            ],
        ),
        migrations.CreateModel(
            name='Propiedades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propiedad', models.CharField(max_length=150)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Articulos')),
            ],
        ),
    ]
