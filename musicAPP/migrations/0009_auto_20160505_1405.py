# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0008_auto_20160504_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='artists',
        ),
        migrations.AddField(
            model_name='track',
            name='artists',
            field=models.ForeignKey(default=1, to='musicAPP.Artist'),
            preserve_default=False,
        ),
    ]
