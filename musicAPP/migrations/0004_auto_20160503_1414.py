# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPP', '0003_auto_20160503_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='country',
            field=models.TextField(null=True, blank=True),
        ),
    ]
