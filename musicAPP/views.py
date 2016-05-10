from django.shortcuts import render
from rest_framework.reverse import reverse

from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics, permissions

from models import *
from forms import *
from serializers import *

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

class CreateArtist(CreateView):
    model = Artist
    template_name = 'form.html'
    form_class = ArtistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateArtist, self).form_valid(form)

class CreateAlbum(CreateView):
    model = Album
    template_name = 'form.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateAlbum, self).form_valid(form)

class CreateTrack(CreateView):
    model = Track
    template_name = 'form.html'
    form_class = TrackForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTrack, self).form_valid(form)

class DeleteArtist(DeleteView):
    model = Artist
    success_url = reverse_lazy('musicapp:artist_list', kwargs={'extension': 'html'})

class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('musicapp:artist_list', kwargs={'extension': 'html'})

class DeleteTrack(DeleteView):
    model = Track
    success_url = reverse_lazy('musicapp:artist_list', kwargs={'extension': 'html'})


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

# RESTfull API views-----------------

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class APIArtistList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class APIArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class APIAlbumList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class APIAlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class APITrackList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Track
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class APITrackDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Track
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
