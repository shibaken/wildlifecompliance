# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-06-18 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0477_auto_20200605_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationselectedactivity',
            name='decision_action',
            field=models.CharField(choices=[('default', 'Default'), ('declined', 'Declined'), ('issued', 'Issued'), ('reissue', 'Re-issue'), ('issue_refund', 'Issued with refund')], default='default', max_length=20, verbose_name='Action'),
        ),
    ]
