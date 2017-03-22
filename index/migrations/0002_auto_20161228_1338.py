# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='Estado',
            field=models.CharField(max_length=20, choices=[('Procesando', 'Procesando'), ('En espera', 'En espera'), ('Terminado', 'Terminado'), ('Entregado', 'Entregado')], default='Procesando'),
        ),
    ]
