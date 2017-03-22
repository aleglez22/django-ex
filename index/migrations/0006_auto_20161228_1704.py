# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20161228_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Apellido',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Cedula',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
