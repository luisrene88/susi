# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20160806_0455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulos',
            options={'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='imagenes',
            options={'verbose_name': 'Imagen', 'verbose_name_plural': 'Imagenes'},
        ),
        migrations.AlterModelOptions(
            name='promocion',
            options={'verbose_name': 'Promocion', 'verbose_name_plural': 'Promociones'},
        ),
        migrations.AlterModelOptions(
            name='propiedades',
            options={'verbose_name': 'Especificacion', 'verbose_name_plural': 'Especificaciones'},
        ),
        migrations.AlterModelOptions(
            name='subcategoria',
            options={'verbose_name': 'Sub Categoria', 'verbose_name_plural': 'Sub Categorias'},
        ),
        migrations.AlterModelOptions(
            name='vistapromocion',
            options={'verbose_name': 'Vista de Promocion', 'verbose_name_plural': 'Vista de Promociones'},
        ),
        migrations.AddField(
            model_name='promocion',
            name='estatus',
            field=models.BooleanField(default=True),
        ),
    ]
