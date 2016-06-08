from django.shortcuts import render
from rest_framework.reverse import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, UpdateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.decorators import method_decorator

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

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not (obj.user == self.request.user or self.request.user.is_superuser):
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'form.html'

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

class CreateArtist(LoginRequiredMixin, CreateView):
    model = Artist
    template_name = 'form.html'
    form_class = ArtistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateArtist, self).form_valid(form)

class CreateAlbum(LoginRequiredMixin, CreateView):
    model = Album
    template_name = 'form.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateAlbum, self).form_valid(form)

class CreateTrack(LoginRequiredMixin, CreateView):
    model = Track
    template_name = 'form.html'
    form_class = TrackForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTrack, self).form_valid(form)

class DeleteArtist(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Artist
    success_url = reverse_lazy('musicapp:artist_list', kwargs={'extension': 'html'})

class DeleteAlbum(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('musicapp:artist_list', kwargs={'extension': 'html'})

class DeleteTrack(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Track
    success_url = reverse_lazy('musicapp:artist_list', kwargs={'extension': 'html'})


@login_required()
def artist_review(request, pk):
    try:
        artist = get_object_or_404(Artist, pk=pk)
        review = ArtistReview(
            rating=request.POST['rating'],
            comment=request.POST['comment'],
            user=request.user,
            artist=artist)
        review.save()
    except:
        pass
    return HttpResponseRedirect(reverse('musicapp:artist_detail', args=(artist.pk,'html')))
@login_required()
def album_review(request, pk):
    try:
        album = get_object_or_404(Album, pk=pk)
        review = AlbumReview(
            rating=request.POST['rating'],
            comment=request.POST['comment'],
            user=request.user,
            album=album)
        review.save()
    except:
        pass
    return HttpResponseRedirect(reverse('musicapp:album_detail', args=(album.pk,'html')))

@login_required()
def track_review(request, pk):
    try:
        track = get_object_or_404(Track, pk=pk)
        review = TrackReview(
            rating=request.POST['rating'],
            comment=request.POST['comment'],
            user=request.user,
            track=track)
        review.save()
    except:
        pass
    return HttpResponseRedirect(reverse('musicapp:track_detail', args=(track.pk,'html')))
