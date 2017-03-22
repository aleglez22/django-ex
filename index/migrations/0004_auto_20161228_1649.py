# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20161228_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='Accesorios',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Estado',
            field=models.CharField(choices=[('PROCESANDO', 'Procesando'), ('ESPERA', 'En espera'), ('TERMINADO', 'Terminado'), ('ENTREGADO', 'Entregado')], default='PROCESANDO', max_length=20),
        ),
    ]
