# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0018_auto_20160517_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.CharField(default=b'album.jpg', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.CharField(default=b'artist.png', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='image',
            field=models.CharField(default=b'track.jpg', max_length=200, null=True),
        ),
    ]
