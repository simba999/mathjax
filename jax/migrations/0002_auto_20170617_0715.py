# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 07:15
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jax', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='explanation',
            field=ckeditor.fields.RichTextField(),
        ),
    ]