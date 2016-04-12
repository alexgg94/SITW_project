from django.forms import ModelForm
import models

class ArtistForm(ModelForm):
    class Meta:
        model = Artist

class AlbumForm(ModelForm):
    class Meta:
        model = Album

class TrackForm(ModelForm):
    class Meta:
        model = Track
