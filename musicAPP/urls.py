from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView, TemplateView

from models import *
from forms import *
from views import *

urlpatterns = patterns('',
    # Home page
    url(r'^$',
        TemplateView.as_view(template_name="home_page.html"),
        name='home_page'),

    # List artists: /musicAPP/artists.json
    url(r'^artists\.(?P<extension>(json|xml|html))$',
        ArtistList.as_view(),
        name='artist_list'),

    # Artist details, ex.: /musicAPP/artists/1.json
    url(r'^artists/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        ArtistDetail.as_view(),
        name='artist_detail'),

    # Create an Artist,  ex.: /musicAPP/artists/create
    url(r'^artists/create.html',
        CreateArtist.as_view(),
        name='createArtist'),

    # Edit Artist, ex.: /musicAPP/artists/1/edit.html
    url(r'^artists/(?P<pk>\d+)/edit.html$',
        UpdateView.as_view(
            model=Artist,
            template_name = "form.html",
            form_class = ArtistForm),
        name='artist_edit'),

    # List albums: /musicAPP/albums.json
    url(r'^albums\.(?P<extension>(json|xml|html))$',
        AlbumList.as_view(),
        name='album_list'),

    # Albums details, ex.: /musicAPP/albums/1.json
    url(r'^albums/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        AlbumDetail.as_view(),
        name='album_detail'),

    # Create an album,  ex.: /musicAPP/albums/create
    url(r'^albums/create.html',
        CreateAlbum.as_view(),
        name='createAlbum'),

    # Edit Album, ex.: /musicAPP/albums/1/edit.html
    url(r'^albums/(?P<pk>\d+)/edit.html$',
        UpdateView.as_view(
            model=Album,
            template_name = "form.html",
            form_class = AlbumForm),
        name='album_edit'),

    # List tracks: /musicAPP/tracks.json
    url(r'^tracks\.(?P<extension>(json|xml|html))$',
        TrackList.as_view(),
        name='track_list'),

    # Tracks details, ex.: /musicAPP/tracks/1.json
    url(r'^tracks/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        TrackDetail.as_view(),
        name='track_detail'),

    # Create a Track,  ex.: /musicAPP/tracks/create
    url(r'^tracks/create.html',
        CreateTrack.as_view(),
        name='createTrack'),

    # Edit Track, ex.: /musicAPP/tracks/1/edit.html
    url(r'^tracks/(?P<pk>\d+)/edit.html$',
        UpdateView.as_view(
            model=Track,
            template_name = "form.html",
            form_class = TrackForm),
        name='track_edit'),

    # User login: /musicAPP/login
    url(r'^login$', 'django.contrib.auth.views.login', name='login'),

    # User logout: /musicAPP/logout
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/musicAPP'}),

    #RESTfull API URLs------------------------

    #List Arists ex.:/api/artists/
    url(r'^api/artists/$',
        APIArtistList.as_view(), name='artist-list'),
    #Arists details ex.:/api/artists/1/
    url(r'^api/artists/(?P<pk>\d+)/$',
        APIArtistDetail.as_view(), name='artist-detail'),

    #List Albums ex.:/api/albums/
    url(r'^api/albums/$',
        APIAlbumList.as_view(), name='album-list'),
    #Album details ex.:/api/albums/1/
    url(r'^api/albums/(?P<pk>\d+)/$',
        APIAlbumDetail.as_view(), name='album-detail'),

    #List Tracks ex.:/api/tracks/
    url(r'^api/tracks/$',
        APITrackList.as_view(), name='track-list'),
    #Tracks detail ex.:/api/tracks/1/
    url(r'^api/tracks/(?P<pk>\d+)/$',
        APITrackDetail.as_view(), name='track-detail'),

)
