# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objbasa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='listing_status',
            field=models.CharField(default='DF', max_length=8, choices=[('DF', 'Draft'), ('AP', 'Approved'), ('BL', 'Blocked')]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='space',
            field=models.CommaSeparatedIntegerField(max_length=6),
        ),
    ]
