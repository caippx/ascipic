# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-31 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ascipic2', '0002_auto_20180331_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='upload_date',
        ),
        migrations.AddField(
            model_name='image',
            name='imgascii',
            field=models.CharField(default=0, max_length=10000),
            preserve_default=False,
        ),
    ]
