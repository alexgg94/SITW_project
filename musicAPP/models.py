from django.db import models

# Create your models here.
class Artist(models.Model):

    name = models.CharField(max_length=50, null=False)
    popularity = models.IntegerField(blank=True)
    spotifyLink = models.URLField(blank=True, null=True)
    #image = models.ImageField()

    def __unicode__(self):
        return u"%s" % self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField('Artist')
    releaseDate = models.DateField()
    spotifyLink = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name


class Track(models.Model):
    name = models.CharField(max_length=50)
    artists = models.ManyToManyField('Artist')
    album = models.ForeignKey('Album')# o varios albums
    spotifyLink = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name


class Review(models.Model):
    RATING_CHOICES = ((1,'Horrible!'),(2,'Bad'),(3,'Good'),(4,'Love it!'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)


class ArtistReview(Review):
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return u"%s - %s" % (self.rating, self.artist.name)

class AlbumReview(Review):
    album = models.ForeignKey(Album)

    def __unicode__(self):
        return u"%s - %s" % (self.rating, self.album.name)

class TrackReview(Review):
    track = models.ForeignKey(Track)

    def __unicode__(self):
        return u"%s - %s" % (self.rating, self.track.name)
