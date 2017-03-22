# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20161228_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Gasto_acumulado',
            field=models.DecimalField(blank=True, max_digits=4, decimal_places=2),
        ),
    ]
