# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-09-18 01:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wildlifecompliance', '0302_weaklinks_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='allegedoffence',
            name='reason_for_removal',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='allegedoffence',
            name='removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='allegedoffence',
            name='removed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alleged_offence_removed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
