# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('didactics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachmenttype',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attachmenttype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 51, 59, 268593), verbose_name='Creation Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attachmenttype',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Is public'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attachmenttype',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 51, 59, 268632), verbose_name='Modify Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 51, 59, 268593), verbose_name='Creation Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Is public'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 51, 59, 268632), verbose_name='Modify Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 51, 59, 268593), verbose_name='Creation Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Is public'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 51, 59, 268632), verbose_name='Modify Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lessonattachment',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lessonattachment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 51, 59, 268593), verbose_name='Creation Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lessonattachment',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Is public'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lessonattachment',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 51, 59, 268632), verbose_name='Modify Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 51, 59, 268593), verbose_name='Creation Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Is public'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 51, 59, 268632), verbose_name='Modify Date'),
            preserve_default=True,
        ),
    ]
