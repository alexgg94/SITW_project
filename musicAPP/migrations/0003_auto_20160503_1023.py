# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0002_auto_20160426_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='country',
            field=models.CharField(default=b'USA', max_length=50),
        ),
        migrations.AlterField(
            model_name='album',
            name='releaseDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
