# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20170105_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='Color',
            field=models.CharField(blank=True, null=True, max_length=20),
        ),
    ]
