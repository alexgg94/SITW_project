# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0013_auto_20160517_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(default=b'/media/album.jpg', null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='track',
            name='image',
            field=models.ImageField(default=b'/media/track.jpg', null=True, upload_to=b''),
        ),
    ]
