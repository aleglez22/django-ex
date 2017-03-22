# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20161228_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='Notas',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
    ]
