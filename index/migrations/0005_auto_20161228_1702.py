# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20161228_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Telefono1',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Telefono2',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='Serial',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='Tipo',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Accesorios',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Costo_reparacion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Costo_revision',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Estado_inicial',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Falla',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Fecha_entrega',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Fecha_ofrecida',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Informe_tecnico',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Limite_garantia',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Notas',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='Apellido',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
