# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('releaseDate', models.DateField()),
                ('spotifyLink', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('popularity', models.IntegerField(blank=True)),
                ('spotifyLink', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=3, verbose_name=b'Ratings (stars)', choices=[(1, b'Horrible!'), (2, b'Bad'), (3, b'Good'), (4, b'Love it!')])),
                ('comment', models.TextField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('spotifyLink', models.URLField(null=True, blank=True)),
                ('album', models.ForeignKey(to='musicAPP.Album')),
                ('artists', models.ManyToManyField(to='musicAPP.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='musicAPP.Review')),
            ],
            bases=('musicAPP.review',),
        ),
        migrations.CreateModel(
            name='ArtistReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='musicAPP.Review')),
                ('artist', models.ForeignKey(to='musicAPP.Artist')),
            ],
            bases=('musicAPP.review',),
        ),
        migrations.CreateModel(
            name='TrackReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='musicAPP.Review')),
                ('track', models.ForeignKey(to='musicAPP.Track')),
            ],
            bases=('musicAPP.review',),
        ),
        migrations.AddField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(to='musicAPP.Artist'),
        ),
        migrations.AddField(
            model_name='albumreview',
            name='album',
            field=models.ForeignKey(to='musicAPP.Album'),
        ),
    ]
