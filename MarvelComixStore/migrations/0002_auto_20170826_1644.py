# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarvelComixStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20, verbose_name='Тег')),
            ],
        ),
        migrations.AlterField(
            model_name='comix',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='comix',
            name='ean',
            field=models.CharField(max_length=13, verbose_name='EAN', serialize=False, unique=True, primary_key=True),
        ),
        migrations.AddField(
            model_name='comix',
            name='tags',
            field=models.ManyToManyField(to='MarvelComixStore.Tag', verbose_name='Теги'),
        ),
    ]
