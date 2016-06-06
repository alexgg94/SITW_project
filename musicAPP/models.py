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
    image = models.CharField(max_length=200, default = "/media/artist.png", null=True)

    def __unicode__(self):
        return u"%s" % self.artist_name
    def get_absolute_url(self):
        return reverse('musicapp:artist_detail', kwargs={'pk': self.pk, 'extension': 'html'})
    def averageRating(self):
        ratingSum = sum([float(review.rating) for review in self.artistreview_set.all()])
        reviewCount = self.artistreview_set.count()
        return int(ratingSum / reviewCount)
    def averageRatingString(self):
        ratingSum = sum([float(review.rating) for review in self.artistreview_set.all()])
        reviewCount = self.artistreview_set.count()
        return Review.RATING_CHOICES[int(ratingSum / reviewCount)-1][1]

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artists = models.ForeignKey('Artist', related_name='albums')
    releaseDate = models.DateField(default=date.today)
    spotifyLink = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    image = models.CharField(max_length=200, default = "/media/album.jpg", null=True)

    def __unicode__(self):
        return u"%s" % self.album_name
    def get_absolute_url(self):
        return reverse('musicapp:album_detail', kwargs={'pk': self.pk, 'extension': 'html'})
    def averageRating(self):
        ratingSum = sum([float(review.rating) for review in self.albumreview_set.all()])
        reviewCount = self.albumreview_set.count()
        return int(ratingSum / reviewCount)
    def averageRatingString(self):
        ratingSum = sum([float(review.rating) for review in self.albumreview_set.all()])
        reviewCount = self.albumreview_set.count()
        return Review.RATING_CHOICES[int(ratingSum / reviewCount)-1][1]

class Track(models.Model):
    track_name = models.CharField(max_length=50)
    artists = models.ForeignKey('Artist')
    album = models.ForeignKey('Album', related_name='tracks')
    spotifyLink = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    image = models.CharField(max_length=200, default = "/media/track.jpg", null=True)

    def __unicode__(self):
        return u"%s" % self.track_name
    def get_absolute_url(self):
        return reverse('musicapp:track_detail', kwargs={'pk': self.pk, 'extension': 'html'})
    def averageRating(self):
        ratingSum = sum([float(review.rating) for review in self.trackreview_set.all()])
        reviewCount = self.trackreview_set.count()
        return int(ratingSum / reviewCount)
    def averageRatingString(self):
        ratingSum = sum([float(review.rating) for review in self.trackreview_set.all()])
        reviewCount = self.trackreview_set.count()
        return Review.RATING_CHOICES[int(ratingSum / reviewCount)-1][1]

class Review(models.Model):
    RATING_CHOICES = ((1,'Horrible!'),(2,'Bad'),(3,'Good'),(4,'Love it!'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, default=1)

    def stringRating(self):
        return self.RATING_CHOICES[self.rating-1][1]

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
