# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 11:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 4, 5, 11, 30, 53, 818485, tzinfo=utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2016, 4, 5, 11, 30, 53, 818526, tzinfo=utc))),
                ('credits_left', models.IntegerField()),
            ],
            options={
                'db_table': 'memberships',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 4, 5, 11, 30, 53, 818485, tzinfo=utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2016, 4, 5, 11, 30, 53, 818526, tzinfo=utc))),
                ('notes_text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'notes',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 4, 5, 11, 30, 53, 818485, tzinfo=utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2016, 4, 5, 11, 30, 53, 818526, tzinfo=utc))),
                ('plan_name', models.CharField(max_length=100)),
                ('credits', models.IntegerField(default=100)),
            ],
            options={
                'db_table': 'plans',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.Plan'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
