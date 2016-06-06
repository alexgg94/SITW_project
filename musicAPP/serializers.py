from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *

class ArtistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:artist-detail')
    #using from Album, the related_name of the artist column
    albums = HyperlinkedRelatedField(many=True, read_only=True, view_name='musicapp:album-detail')
    user = CharField(read_only=True)
    artistsReviews = HyperlinkedRelatedField(many=True, read_only=True, view_name='musicapp:artist-review-detail')

    class Meta:
        model = Artist
        fields = ('uri', 'artist_name', 'country', 'popularity', 'image',
                  'spotifyLink', 'user', 'albums', 'artistsReviews')

class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:album-detail')
    artists = HyperlinkedRelatedField(read_only=True, view_name='musicapp:artist-detail')
    tracks = HyperlinkedRelatedField(many=True, read_only=True, view_name='musicapp:track-detail')
    user = CharField(read_only=True)
    albumsReviews = HyperlinkedRelatedField(many=True, read_only=True, view_name='musicapp:album-review-detail')

    class Meta:
        model = Album
        fields = ('uri', 'album_name', 'artists', 'releaseDate', 'image',
                  'spotifyLink', 'user', 'tracks', 'albumsReviews')

class TrackSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:track-detail')
    artists = HyperlinkedRelatedField(read_only=True, view_name='musicapp:artist-detail')
    album = HyperlinkedRelatedField(read_only=True, view_name='musicapp:album-detail')
    user = CharField(read_only=True)
    tracksReviews = HyperlinkedRelatedField(many=True, read_only=True, view_name='musicapp:track-review-detail')

    class Meta:
        model = Track
        fields = ('uri', 'track_name', 'artists', 'album', 'image',
                  'spotifyLink', 'user', 'tracksReviews')

class ArtistReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:artist-review-detail')
    artist = HyperlinkedRelatedField(view_name='musicapp:artist-detail', read_only=True)
    user = CharField(read_only=True)
    stringRating = CharField(read_only=True)

    class Meta:
        model = ArtistReview
        fields = ('uri', 'rating', 'stringRating', 'comment', 'user', 'date', 'artist')

class AlbumReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:album-review-detail')
    album = HyperlinkedRelatedField(view_name='musicapp:album-detail', read_only=True)
    user = CharField(read_only=True)
    stringRating = CharField(read_only=True)

    class Meta:
        model = AlbumReview
        fields = ('uri', 'rating', 'stringRating', 'comment', 'user', 'date', 'album')


class TrackReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:track-review-detail')
    track = HyperlinkedRelatedField(view_name='musicapp:track-detail', read_only=True)
    user = CharField(read_only=True)
    stringRating = CharField(read_only=True)

    class Meta:
        model = TrackReview
        fields = ('uri', 'rating', 'stringRating', 'comment', 'user', 'date', 'track')
