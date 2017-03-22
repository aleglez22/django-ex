# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20170213_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Cedula',
            field=models.IntegerField(),
        ),
    ]
