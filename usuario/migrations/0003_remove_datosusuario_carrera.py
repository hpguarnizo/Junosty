# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-30 07:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20161020_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosusuario',
            name='carrera',
        ),
    ]
