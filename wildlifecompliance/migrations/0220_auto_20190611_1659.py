# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-06-11 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0219_remove_callemail_allocated_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regiondistrict',
            name='district',
            field=models.CharField(choices=[('SWAN', 'Swan Region'), ('PHD', 'Perth Hills'), ('SCD', 'Swan Coastal'), ('SWR', 'South West Region'), ('BWD', 'Blackwood'), ('WTN', 'Wellington'), ('WR', 'Warren Region'), ('DON', 'Donnelly'), ('FRK', 'Frankland'), ('SCR', 'South Coast Region'), ('ALB', 'Albany'), ('ESP', 'Esperance'), ('KIMB', 'Kimberley Region'), ('EKD', 'East Kimberley'), ('WKD', 'West Kimberley'), ('PIL', 'Pilbara Region'), ('EXM', 'Exmouth'), ('GLD', 'Goldfields Region'), ('MWR', 'Midwest Region'), ('GER', 'Geraldton'), ('KLB', 'Kalbarri'), ('MOR', 'Moora'), ('SHB', 'Shark Bay'), ('WBR', 'Wheatbelt Region'), ('CWB', 'Central Wheatbelt'), ('SWB', 'Southern Wheatbelt'), ('AV', 'Aviation'), ('OTH', 'Other'), ('KENSINGTON', 'Kensington')], default='OTH', max_length=32),
        ),
    ]
