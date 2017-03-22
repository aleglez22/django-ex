# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_auto_20170214_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='ID', default=1, primary_key=True, auto_created=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Cedula',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
