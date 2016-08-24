# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 07:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=300, verbose_name='Category Name')),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='CategoryInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
                ('sugestion_text', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aangan_report.Category', verbose_name='Category Id')),
            ],
            options={
                'db_table': 'category_instance',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=200, verbose_name='Question Name')),
                ('formula', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aangan_report.Category', verbose_name='Category Id')),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='QuestionInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aangan_report.Question', verbose_name='Question Id')),
            ],
            options={
                'db_table': 'question_instance',
            },
        ),
        migrations.CreateModel(
            name='ReportInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('doj', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Of Joining')),
            ],
            options={
                'db_table': 'report_instance',
            },
        ),
        migrations.CreateModel(
            name='ScoringSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
            ],
            options={
                'db_table': 'scoring_schema',
            },
        ),
        migrations.AddField(
            model_name='questioninstance',
            name='report_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aangan_report.ReportInstance', verbose_name='Report Instance Id'),
        ),
        migrations.AddField(
            model_name='categoryinstance',
            name='report_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aangan_report.ReportInstance', verbose_name='Report Instance Id'),
        ),
    ]