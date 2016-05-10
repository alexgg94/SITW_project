from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView, TemplateView

from rest_framework.urlpatterns import format_suffix_patterns

from models import *
from forms import *
from views import *

urlpatterns = [
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
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Artist,
            form_class = ArtistForm),
        name='artist_edit'),

    #Delete an Artist ex.:/musicAPP/artists/1/delete/
    url(r'^artists/(?P<pk>\d+)/delete.html$',
    DeleteArtist.as_view(),
    name='artist_delete'),

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
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Album,
            form_class = AlbumForm),
        name='album_edit'),

    #Delete an Album ex.:/musicAPP/albums/1/delete/
    url(r'^albums/(?P<pk>\d+)/delete.html$',
    DeleteAlbum.as_view(),
    name='album_delete'),

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
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Track,
            form_class = TrackForm),
        name='track_edit'),

    #Delete an Track ex.:/musicAPP/tracks/1/delete/
    url(r'^tracks/(?P<pk>\d+)/delete.html$',
    DeleteTrack.as_view(),
    name='track_delete'),


    #RESTfull API URLs------------------------
    url(r'api/', include('musicAPP.urls_api')),

]
