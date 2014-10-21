# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='view',
            name='page',
            field=models.ForeignKey(to='analytics.Page'),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('city', 'country')]),
        ),
    ]
