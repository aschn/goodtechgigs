# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150305_2200'),
        ('tags', '0002_auto_20150305_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', model_utils.fields.StatusField(default=b'draft', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'draft', b'draft'), (b'published', b'published'), (b'expired', b'expired'), (b'removed', b'removed')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('poster', models.ForeignKey(to='profiles.GigPoster')),
                ('skills_desired', taggit.managers.TaggableManager(to='tags.SkillTag', through='tags.SkillTaggedItem', help_text='A comma-separated list of tags.', verbose_name=b'desired skills')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
