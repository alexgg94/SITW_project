from django.forms import ModelForm
from models import *

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('user',)

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ('user',)

class TrackForm(ModelForm):
    class Meta:
        model = Track
        exclude = ('user',)
