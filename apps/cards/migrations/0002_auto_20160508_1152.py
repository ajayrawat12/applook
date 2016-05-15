# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='uplaod_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'time'),
        ),
    ]
