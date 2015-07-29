# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acronym',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('short_text', models.CharField(max_length=10)),
                ('long_text', models.CharField(max_length=200)),
                ('pub_date', models.DateField(blank=True, verbose_name='date created')),
                ('realm', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=2000)),
                ('ref', models.URLField(blank=True, max_length=2000)),
            ],
        ),
    ]
