from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

from models import *
from forms import *
from views import *

urlpatterns = patterns('',
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('musicapp:artist_list', kwargs={'extension': 'html'})),
        name='home_page'),

    # List artists: /musicAPP/artists.json
    url(r'^artists\.(?P<extension>(json|xml|html))$',
        ArtistList.as_view(),
        name='artist_list'),

    # Artist details, ex.: /musicAPP/artists/1.json
    url(r'^artists/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        ArtistDetail.as_view(),
        name='artist_detail'),


    # List albums: /musicAPP/albums.json
    url(r'^albums\.(?P<extension>(json|xml|html))$',
        AlbumList.as_view(),
        name='album_list'),

    # Albums details, ex.: /musicAPP/albums/1.json
    url(r'^albums/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        AlbumDetail.as_view(),
        name='album_detail'),


    # List tracks: /musicAPP/tracks.json
    url(r'^tracks\.(?P<extension>(json|xml|html))$',
        TrackList.as_view(),
        name='track_list'),

    # Tracks details, ex.: /musicAPP/tracks/1.json
    url(r'^tracks/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        TrackDetail.as_view(),
        name='track_detail'),

)