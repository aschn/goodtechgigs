# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causetaggeditem',
            name='tag',
            field=models.ForeignKey(related_name='tags_causetaggeditem_causes', to='tags.CauseTag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='skilltaggeditem',
            name='tag',
            field=models.ForeignKey(related_name='tags_skilltaggeditem_skills', to='tags.SkillTag'),
            preserve_default=True,
        ),
    ]
