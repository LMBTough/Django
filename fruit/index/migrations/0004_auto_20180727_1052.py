# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-27 02:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180723_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.Author')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='Publisher',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 27, 10, 52, 51, 70228)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='名字'),
        ),
    ]
