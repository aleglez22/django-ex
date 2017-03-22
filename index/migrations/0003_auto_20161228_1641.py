# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20161228_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='Estado',
            field=models.CharField(default='ESPERA', max_length=20, choices=[('PROCESANDO', 'Procesando'), ('ESPERA', 'En espera'), ('TERMINADO', 'Terminado'), ('ENTREGADO', 'Entregado')]),
        ),
    ]
