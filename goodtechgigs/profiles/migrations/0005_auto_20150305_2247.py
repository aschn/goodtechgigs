# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150305_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gigposter',
            name='org_name',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
