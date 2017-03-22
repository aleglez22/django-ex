# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20170105_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='Cliente',
            field=models.ForeignKey(on_delete=models.SET(index.models.get_sentinel_user), to='index.Cliente'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Equipo',
            field=models.ForeignKey(on_delete=models.SET(index.models.get_sentinel_user), to='index.Equipo'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Tecnico',
            field=models.ForeignKey(on_delete=models.SET(index.models.get_sentinel_user), to='index.Tecnico'),
        ),
    ]
