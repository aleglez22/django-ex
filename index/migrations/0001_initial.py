# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('Cedula', models.CharField(max_length=10)),
                ('Fecha_ingreso', models.DateField(auto_now=True)),
                ('Gasto_acumulado', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Telefono1', models.IntegerField()),
                ('Telefono2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Marca', models.CharField(max_length=30)),
                ('Modelo', models.CharField(max_length=30)),
                ('Serial', models.CharField(max_length=40)),
                ('Tipo', models.CharField(max_length=20)),
                ('Cliente', models.ForeignKey(to='index.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Fecha_creacion', models.DateField(auto_now=True)),
                ('Fecha_entrega', models.DateField()),
                ('Estado_inicial', models.CharField(max_length=250)),
                ('Falla', models.CharField(max_length=250)),
                ('Costo_reparacion', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Costo_revision', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Notas', models.DateField()),
                ('Fecha_ofrecida', models.DateField()),
                ('Accesorios', models.DateField()),
                ('Limite_garantia', models.CharField(max_length=20)),
                ('Informe_tecnico', models.CharField(max_length=250)),
                ('Estado', models.CharField(max_length=20, default='Procesando', choices=[('PROCESANDO', 'Procesando'), ('ESPERA', 'En espera'), ('TERMINADO', 'Terminado'), ('ENTREGADO', 'Entregado')])),
                ('Cliente', models.ForeignKey(to='index.Cliente')),
                ('Equipo', models.ForeignKey(to='index.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('Fecha_ingreso', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='Tecnico',
            field=models.ForeignKey(to='index.Tecnico'),
        ),
    ]
