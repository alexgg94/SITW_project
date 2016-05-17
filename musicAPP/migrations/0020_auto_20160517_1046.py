# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0019_auto_20160517_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='image',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='image',
        ),
        migrations.RemoveField(
            model_name='track',
            name='image',
        ),
    ]
