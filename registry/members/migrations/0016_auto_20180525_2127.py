# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_auto_20180525_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='date_of_birth',
            new_name='Date_of_Birth',
        ),
    ]
