# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-02-11 06:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0420_auto_20200211_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProsecutionBriefDocumentArtifacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProsecutionBriefPhysicalArtifacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticked', models.BooleanField(default=False)),
                ('legal_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.LegalCase')),
            ],
        ),
        migrations.RemoveField(
            model_name='physicalartifact',
            name='sensitive_non_disclosable',
        ),
        migrations.RemoveField(
            model_name='physicalartifact',
            name='used_within_case',
        ),
        migrations.AddField(
            model_name='documentartifact',
            name='brief_of_evidence_legal_cases',
            field=models.ManyToManyField(related_name='legal_case_document_artifacts_brief_of_evidence', through='wildlifecompliance.BriefOfEvidenceDocumentArtifacts', to='wildlifecompliance.LegalCase'),
        ),
        migrations.AddField(
            model_name='physicalartifact',
            name='brief_of_evidence_legal_cases',
            field=models.ManyToManyField(related_name='legal_case_physical_artifacts_brief_of_evidence', through='wildlifecompliance.BriefOfEvidencePhysicalArtifacts', to='wildlifecompliance.LegalCase'),
        ),
        migrations.AlterField(
            model_name='briefofevidencedocumentartifacts',
            name='document_artifact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.DocumentArtifact'),
        ),
        migrations.AlterField(
            model_name='briefofevidencedocumentartifacts',
            name='legal_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.LegalCase'),
        ),
        migrations.AlterField(
            model_name='briefofevidencephysicalartifacts',
            name='legal_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.LegalCase'),
        ),
        migrations.AlterField(
            model_name='briefofevidencephysicalartifacts',
            name='physical_artifact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.PhysicalArtifact'),
        ),
        migrations.AddField(
            model_name='prosecutionbriefphysicalartifacts',
            name='physical_artifact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.PhysicalArtifact'),
        ),
        migrations.AddField(
            model_name='prosecutionbriefdocumentartifacts',
            name='document_artifact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.DocumentArtifact'),
        ),
        migrations.AddField(
            model_name='prosecutionbriefdocumentartifacts',
            name='legal_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.LegalCase'),
        ),
        migrations.AddField(
            model_name='documentartifact',
            name='prosecution_brief_legal_cases',
            field=models.ManyToManyField(related_name='legal_case_document_artifacts_prosecution_brief', through='wildlifecompliance.ProsecutionBriefDocumentArtifacts', to='wildlifecompliance.LegalCase'),
        ),
        migrations.AddField(
            model_name='physicalartifact',
            name='prosecution_brief_legal_cases',
            field=models.ManyToManyField(related_name='legal_case_physical_artifacts_prosecution_brief', through='wildlifecompliance.ProsecutionBriefPhysicalArtifacts', to='wildlifecompliance.LegalCase'),
        ),
    ]