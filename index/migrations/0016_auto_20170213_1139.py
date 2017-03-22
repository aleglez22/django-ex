# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_equipo_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='Direccion',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Email',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Notas',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
