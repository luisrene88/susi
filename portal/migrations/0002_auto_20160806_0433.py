# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 04:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('estatus', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('estatus', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Categoria')),
            ],
        ),
        migrations.AlterField(
            model_name='imagenes',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img_articulos', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='subcategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.SubCategoria'),
        ),
    ]