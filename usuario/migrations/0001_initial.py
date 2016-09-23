# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-19 00:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='datosusuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('no_boleta', models.CharField(max_length=10)),
                ('curp', models.CharField(max_length=18)),
                ('carrera', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]