# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_auto_20180525_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='Date_of_Birth',
            field=models.DateField(null=True),
        ),
    ]
