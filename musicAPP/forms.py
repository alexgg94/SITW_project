from django.forms import ModelForm
from models import *

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('spotifyLink','user',)

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ('spotifyLink','user',)

class TrackForm(ModelForm):
    class Meta:
        model = Track
        exclude = ('spotifyLink','user',)
