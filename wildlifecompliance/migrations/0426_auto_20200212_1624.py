# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-02-12 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0425_merge_20200210_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationselectedactivity',
            name='additional_fee',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=8),
        ),
        migrations.AddField(
            model_name='applicationselectedactivity',
            name='additional_fee_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
