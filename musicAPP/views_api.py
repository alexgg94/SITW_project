from django.shortcuts import render
from rest_framework.reverse import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.decorators import method_decorator

from rest_framework import generics, permissions

from models import *
from forms import *
from serializers import *
from views import LoginRequiredMixin

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user

#---------------- API Artists views ----------------
class APIArtistList(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class APIArtistDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class APIArtistReviewList(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = ArtistReview
    queryset = ArtistReview.objects.all()
    serializer_class = ArtistReviewSerializer

class APIArtistReviewDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = ArtistReview
    queryset = ArtistReview.objects.all()
    serializer_class = ArtistReviewSerializer

#---------------- API Albums views ----------------
class APIAlbumList(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class APIAlbumDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class APIAlbumReviewList(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = AlbumReview
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer

class APIAlbumReviewDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = AlbumReview
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer

#---------------- API Artists views ----------------
class APITrackList(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Track
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class APITrackDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Track
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class APITrackReviewList(LoginRequiredMixin, generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = TrackReview
    queryset = TrackReview.objects.all()
    serializer_class = TrackReviewSerializer

class APITrackReviewDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = TrackReview
    queryset = TrackReview.objects.all()
    serializer_class = TrackReviewSerializer
