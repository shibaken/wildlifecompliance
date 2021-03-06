# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-01-07 06:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0365_auto_20200106_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artifact',
            name='status',
            field=models.CharField(choices=[('active', 'Open'), ('waiting_for_disposal', 'Waiting For Disposal'), ('closed', 'Closed')], default='active', max_length=100),
        ),
    ]
