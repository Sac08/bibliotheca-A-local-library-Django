# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20170928_1012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
