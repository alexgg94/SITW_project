from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Artist, Album, Track

class ArtistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:artist-detail')
    #using from Album, the related_name of the artist column
    albums = HyperlinkedRelatedField(many=True, read_only=True, view_name='musicapp:album-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Artist
        fields = ('uri', 'artist_name', 'country', 'popularity', 'spotifyLink', 'user', 'albums')

class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:album-detail')
    artists = HyperlinkedRelatedField(read_only=True, view_name='musicapp:artist-detail')
    tracks = HyperlinkedRelatedField(many=True, read_only=True, view_name='musicapp:track-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Album
        fields = ('uri', 'album_name', 'artists', 'releaseDate', 'spotifyLink', 'user', 'tracks')

class TrackSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='musicapp:track-detail')
    artists = HyperlinkedRelatedField(read_only=True, view_name='musicapp:artist-detail')
    album = HyperlinkedRelatedField(read_only=True, view_name='musicapp:album-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Track
        fields = ('uri', 'track_name', 'artists', 'album', 'spotifyLink', 'user', )
