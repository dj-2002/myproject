# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-23 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdbtest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_dob',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
