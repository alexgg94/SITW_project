from django.shortcuts import render

from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView

from models import *
from forms import *

class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        return super(ConnegResponseMixin, self).render_to_response(context)

class ArtistList(ListView, ConnegResponseMixin):
    model = Artist
    template_name = 'artist_list.html'

class ArtistDetail(DetailView, ConnegResponseMixin):
    model = Artist
    template_name = 'artist_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        context["albums"] = Album.objects.filter(artists=self.get_object())
        context['RATING_CHOICES'] = ArtistReview.RATING_CHOICES
        return context

class AlbumList(ListView, ConnegResponseMixin):
    model = Album
    template_name = 'album_list.html'

class AlbumDetail(DetailView, ConnegResponseMixin):
    model = Album
    template_name = 'album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context["tracks"] = Track.objects.filter(album=self.get_object())
        context['RATING_CHOICES'] = AlbumReview.RATING_CHOICES
        return context

class TrackList(ListView, ConnegResponseMixin):
    model = Track
    template_name = 'track_list.html'

class TrackDetail(DetailView, ConnegResponseMixin):
    model = Track
    template_name = 'track_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TrackDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = TrackReview.RATING_CHOICES
        return context

"""
def review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    review = RestaurantReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        restaurant=restaurant)
    review.save()
    return HttpResponseRedirect(reverse('myrestaurants:restaurant_detail', args=(restaurant.id,)))
"""
