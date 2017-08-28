# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('MarvelComixStore', '0002_auto_20170826_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to=settings.AUTH_USER_MODEL, serialize=False)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='comix',
            name='date',
            field=models.DateField(verbose_name='Дата выхода', db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='comixlist',
            field=models.ManyToManyField(to='MarvelComixStore.Comix'),
        ),
    ]
