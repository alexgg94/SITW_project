from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView, TemplateView

from rest_framework.urlpatterns import format_suffix_patterns

from models import *
from forms import *
from views import *


urlpatterns = patterns('',
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

)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'xml', 'json'])
