# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-01-02 06:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0358_auto_20191224_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmendmentRequestForRemediationAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(blank=True, max_length=100)),
                ('details', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CM_AmendmentRequest',
                'verbose_name_plural': 'CM_AmendmentRequests',
            },
        ),
        migrations.CreateModel(
            name='AmendmentRequestReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CM_AmendmentRequestReason',
                'verbose_name_plural': 'CM_AmendmentRequestReasons',
            },
        ),
        migrations.AlterField(
            model_name='remediationaction',
            name='status',
            field=models.CharField(blank=True, choices=[(b'open', b'Open'), (b'overdue', b'Overdue'), (b'submitted', b'Submitted'), (b'accepted', b'Accepted')], default=b'open', max_length=40),
        ),
        migrations.AddField(
            model_name='amendmentrequestforremediationaction',
            name='remediation_action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amendment_requests', to='wildlifecompliance.RemediationAction'),
        ),
    ]
