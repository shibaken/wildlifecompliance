# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-02-07 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0418_auto_20200206_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legalcase',
            name='court_proceedings',
        ),
        migrations.AddField(
            model_name='courtproceedings',
            name='legal_case',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='court_proceedings', to='wildlifecompliance.LegalCase'),
        ),
    ]
