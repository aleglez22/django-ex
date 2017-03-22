# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_equipo_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='Cliente',
            field=models.ForeignKey(to='index.Cliente', on_delete=django.db.models.deletion.DO_NOTHING),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Cliente',
            field=models.ForeignKey(to='index.Cliente', on_delete=django.db.models.deletion.DO_NOTHING),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Equipo',
            field=models.ForeignKey(to='index.Equipo', on_delete=django.db.models.deletion.DO_NOTHING),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Tecnico',
            field=models.ForeignKey(to='index.Tecnico', on_delete=django.db.models.deletion.DO_NOTHING),
        ),
    ]
