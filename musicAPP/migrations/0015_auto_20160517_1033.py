# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0014_auto_20160517_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(default=b'album.jpg', null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(default=b'artist.png', null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='track',
            name='image',
            field=models.ImageField(default=b'track.jpg', null=True, upload_to=b''),
        ),
    ]
