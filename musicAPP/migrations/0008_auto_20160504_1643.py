# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0007_auto_20160504_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artists',
        ),
        migrations.AddField(
            model_name='album',
            name='artists',
            field=models.ForeignKey(related_name='albums', default=1, to='musicAPP.Artist'),
            preserve_default=False,
        ),
    ]
