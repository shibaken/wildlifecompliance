# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-08-25 02:36
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0508_wildlifelicence_property_cache'),
    ]

    operations = [
        migrations.AddField(
            model_name='return',
            name='property_cache',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
    ]
