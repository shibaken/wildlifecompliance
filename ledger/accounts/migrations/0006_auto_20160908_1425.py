# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-08 06:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_duplicates'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('user', 'hash')]),
        ),
    ]
