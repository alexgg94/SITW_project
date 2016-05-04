# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0005_auto_20160503_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='name',
            new_name='album_name',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='name',
            new_name='artist_name',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='name',
            new_name='track_name',
        ),
    ]
