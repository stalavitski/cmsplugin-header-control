# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 03:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0015_auto_20160421_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderControlPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('cache_duration', models.PositiveIntegerField(default=60, help_text='Provide the duration (in seconds) that this content should be considered valid.', verbose_name='cache duration')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='HTTPHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_name', models.CharField(default='', max_length=250, verbose_name='header name')),
            ],
        ),
        migrations.AddField(
            model_name='headercontrolpluginmodel',
            name='headers',
            field=models.ManyToManyField(blank=True, default=None, to='cmsplugin_header_control.HTTPHeader'),
        ),
    ]
