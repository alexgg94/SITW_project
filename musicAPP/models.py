from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.urlresolvers import reverse

# Create your models here.
class Artist(models.Model):

    artist_name = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=True)
    popularity = models.IntegerField(blank=True)
    spotifyLink = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    #image = models.ImageField()

    def __unicode__(self):
        return u"%s" % self.artist_name
    def get_absolute_url(self):
        return reverse('musicapp:artist_detail', kwargs={'pk': self.pk, 'extension': 'html'})


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artists = models.ManyToManyField('Artist', related_name='albums')
    releaseDate = models.DateField(default=date.today)
    spotifyLink = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.album_name
    def get_absolute_url(self):
        return reverse('musicapp:album_detail', kwargs={'pk': self.pk, 'extension': 'html'})


class Track(models.Model):
    track_name = models.CharField(max_length=50)
    artists = models.ManyToManyField('Artist')
    album = models.ForeignKey('Album')
    spotifyLink = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.track_name
    def get_absolute_url(self):
        return reverse('musicapp:track_detail', kwargs={'pk': self.pk, 'extension': 'html'})


class Review(models.Model):
    RATING_CHOICES = ((1,'Horrible!'),(2,'Bad'),(3,'Good'),(4,'Love it!'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, default=1)


class ArtistReview(Review):
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return u"%s - %s" % (self.rating, self.artist.artist_name)

class AlbumReview(Review):
    album = models.ForeignKey(Album)

    def __unicode__(self):
        return u"%s - %s" % (self.rating, self.album.album_name)

class TrackReview(Review):
    track = models.ForeignKey(Track)

    def __unicode__(self):
        return u"%s - %s" % (self.rating, self.track.track_name)
