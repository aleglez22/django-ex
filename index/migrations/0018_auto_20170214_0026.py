# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0017_auto_20170214_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Cedula',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, max_length=10),
        ),
    ]
