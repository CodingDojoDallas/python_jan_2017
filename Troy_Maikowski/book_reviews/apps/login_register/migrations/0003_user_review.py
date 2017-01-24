# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('login_register', '0002_auto_20170119_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Review'),
        ),
    ]
