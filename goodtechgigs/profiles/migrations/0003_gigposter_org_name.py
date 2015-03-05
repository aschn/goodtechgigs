# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150305_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='gigposter',
            name='org_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
