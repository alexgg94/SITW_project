# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0020_auto_20160517_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.CharField(default=b'/media/album.jpg', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.CharField(default=b'/media/artist.png', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='image',
            field=models.CharField(default=b'/media/track.jpg', max_length=200, null=True),
        ),
    ]
