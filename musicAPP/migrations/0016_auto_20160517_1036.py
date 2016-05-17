# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0015_auto_20160517_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.URLField(default=b'album.jpg', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.URLField(default=b'artist.png', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='image',
            field=models.URLField(default=b'track.jpg', null=True, blank=True),
        ),
    ]
