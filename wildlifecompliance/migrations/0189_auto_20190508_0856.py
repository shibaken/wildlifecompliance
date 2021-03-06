# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-05-08 00:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0188_auto_20190508_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callemail',
            name='classification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='call_classification', to='wildlifecompliance.Classification'),
        ),
        migrations.AlterField(
            model_name='callemail',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='call_location', to='wildlifecompliance.Location'),
        ),
    ]
