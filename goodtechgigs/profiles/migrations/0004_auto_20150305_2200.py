# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_gigposter_org_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gigposter',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gigposter',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gigseeker',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gigseeker',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gigposter',
            name='causes',
            field=taggit.managers.TaggableManager(to='tags.CauseTag', through='tags.CauseTaggedItem', help_text='A comma-separated list of tags.', verbose_name=b'causes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gigseeker',
            name='causes',
            field=taggit.managers.TaggableManager(to='tags.CauseTag', through='tags.CauseTaggedItem', help_text='A comma-separated list of tags.', verbose_name=b'causes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gigseeker',
            name='skills',
            field=taggit.managers.TaggableManager(to='tags.SkillTag', through='tags.SkillTaggedItem', help_text='A comma-separated list of tags.', verbose_name=b'skills'),
            preserve_default=True,
        ),
    ]
