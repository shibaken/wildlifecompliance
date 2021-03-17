# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-17 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0538_auto_20210305_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='name',
            field=models.CharField(choices=[('complaint', 'Complaint'), ('enquiry', 'Enquiry'), ('incident', 'Incident')], default='complaint', max_length=30, unique=True),
        ),
    ]
