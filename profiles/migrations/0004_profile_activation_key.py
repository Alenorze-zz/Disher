# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activation_key',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
