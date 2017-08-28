# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comix',
            fields=[
                ('name', models.CharField(verbose_name='Имя', max_length=100)),
                ('description', models.CharField(verbose_name='Описание', max_length=100)),
                ('date', models.DateField(editable=False, default=django.utils.timezone.now, db_index=True, verbose_name='Дата выхода')),
                ('ean', models.BigIntegerField(serialize=False, primary_key=True, unique=True, verbose_name='EAN')),
                ('cover', models.ImageField(upload_to='', verbose_name='Обложка')),
            ],
        ),
    ]
