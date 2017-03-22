# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20170103_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='Fecha_creacion',
            field=models.DateField(auto_now=True, default=datetime.datetime(2017, 1, 4, 19, 0, 14, 237720)),
            preserve_default=False,
        ),
    ]
