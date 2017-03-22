# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0019_auto_20170214_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Cedula',
            field=models.IntegerField(unique=True),
        ),
    ]
