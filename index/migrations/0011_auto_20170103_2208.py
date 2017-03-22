# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20161229_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='Costo_reparacion',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=6),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Costo_revision',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=6),
        ),
    ]
