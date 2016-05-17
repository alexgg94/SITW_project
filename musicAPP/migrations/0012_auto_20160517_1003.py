# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0011_auto_20160510_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(default=b'media/album.jpg', upload_to=b''),
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(default=b'media/artist.png', upload_to=b''),
        ),
        migrations.AddField(
            model_name='track',
            name='image',
            field=models.ImageField(default=b'media/track.jpg', upload_to=b''),
        ),
    ]
