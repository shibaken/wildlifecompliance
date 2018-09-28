# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-07 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0033_updateviews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mooringarea',
            options={'verbose_name': 'Mooring', 'verbose_name_plural': 'Moorings'},
        ),
        migrations.AlterModelOptions(
            name='mooringareagroup',
            options={'verbose_name': 'Mooring Group', 'verbose_name_plural': 'Mooring Groups'},
        ),
        migrations.RenameField(
            model_name='mooringareagroup',
            old_name='campgrounds',
            new_name='moorings',
        ),
        migrations.AlterField(
            model_name='mooringarea',
            name='price_level',
            field=models.SmallIntegerField(choices=[(0, 'Mooring level')], default=0),
        ),
        migrations.AlterField(
            model_name='mooringarea',
            name='site_type',
            field=models.SmallIntegerField(choices=[(0, 'Bookable Per Site')], default=0),
        ),
        migrations.AlterField(
            model_name='mooringsiterate',
            name='update_level',
            field=models.SmallIntegerField(choices=[(0, 'Mooring level'), (1, 'Mooring site Class level'), (2, 'Mooring site level')], default=0),
        ),
        migrations.AlterModelTable(
            name='mooringsiteclasspricehistory',
            table='mooring_mooringsiteclass_pricehistory_v',
        ),
    ]
