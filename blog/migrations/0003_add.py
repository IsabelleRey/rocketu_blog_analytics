# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141018_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_url', models.URLField()),
                ('add_name', models.CharField(max_length=20, null=True, blank=True)),
                ('add_image', models.ImageField(upload_to=b'static/img/add_image', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
