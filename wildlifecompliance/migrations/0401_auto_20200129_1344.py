# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-01-29 05:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0400_auto_20200124_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='briefofevidencerecordofinterview',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='wildlifecompliance.BriefOfEvidenceRecordOfInterview'),
        ),
        migrations.AlterField(
            model_name='legalcase',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('await_endorsement', 'Awaiting Endorsement'), ('discarded', 'Discarded'), ('brief_of_evidence', 'Brief of Evidence'), ('closed', 'Closed'), ('pending_closure', 'Pending Closure')], default='open', max_length=100),
        ),
    ]
