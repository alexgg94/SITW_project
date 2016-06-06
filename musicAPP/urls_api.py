from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView, TemplateView

from rest_framework.urlpatterns import format_suffix_patterns

from models import *
from forms import *
from views_api import *


urlpatterns = [
    #RESTfull API URLs------------------------
        url(r'^$',
            TemplateView.as_view(template_name="home_page_api.html"),
            name='home_page_api'),
        #List Arists ex.:/artists/
        url(r'^artists/$',
            APIArtistList.as_view(), name='artist-list'),
        #Arists details ex.:/artists/1/
        url(r'^artists/(?P<pk>\d+)/$',
            APIArtistDetail.as_view(), name='artist-detail'),

        #List Albums ex.:/albums/
        url(r'^albums/$',
            APIAlbumList.as_view(), name='album-list'),
        #Album details ex.:/albums/1/
        url(r'^albums/(?P<pk>\d+)/$',
            APIAlbumDetail.as_view(), name='album-detail'),

        #List Tracks ex.:/tracks/
        url(r'^tracks/$',
            APITrackList.as_view(), name='track-list'),
        #Tracks detail ex.:/tracks/1/
        url(r'^tracks/(?P<pk>\d+)/$',
            APITrackDetail.as_view(), name='track-detail'),

        #List Artists reviews ex.:/artistsReviews/
        url(r'^artistsReviews/$',
            APIArtistReviewList.as_view(), name='artist-review-list'),
        #Artists review detail ex.:/artistsReviews/1/
        url(r'^artistsReviews/(?P<pk>\d+)/$',
            APIArtistReviewDetail.as_view(), name='artist-review-detail'),

        #List Albums reviews ex.:/albumsReviews/
        url(r'^albumsReviews/$',
            APIAlbumReviewList.as_view(), name='album-review-list'),
        #Albums review detail ex.:/albumsReviews/1/
        url(r'^albumsReviews/(?P<pk>\d+)/$',
            APIAlbumReviewDetail.as_view(), name='album-review-detail'),

        #List Tracks reviews ex.:/tracksReviews/
        url(r'^tracksReviews/$',
            APITrackReviewList.as_view(), name='track-review-list'),
        #Tracks review detail ex.:/tracksReviews/1/
        url(r'^tracksReviews/(?P<pk>\d+)/$',
            APITrackReviewDetail.as_view(), name='track-review-detail')

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'xml', 'json'])
