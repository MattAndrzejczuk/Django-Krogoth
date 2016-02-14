# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='description',
            field=models.TextField(max_length=400, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
