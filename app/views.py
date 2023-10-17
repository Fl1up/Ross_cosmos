from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Artist, Album, Track
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer, ArtistCreateSerializer, \
    AlbumCreateSerializer, TrackCreateSerializer


class ArtistCreateAPIView(generics.CreateAPIView):
    """Factors Create"""
    serializer_class = ArtistCreateSerializer


class ArtistListAPIView(generics.ListAPIView):
    """Factors List"""
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class ArtistRetrieveAPIView(generics.RetrieveAPIView):
    """Factors Retrive"""
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class ArtistUpdateAPIView(generics.UpdateAPIView):
    """Factors Updaate"""
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class ArtistDestroyAPIView(generics.DestroyAPIView):
    """Album Delete"""
    queryset = Artist.objects.all()


class AlbumCreateAPIView(generics.CreateAPIView):
    """Album Create"""
    serializer_class = AlbumCreateSerializer


class AlbumListAPIView(generics.ListAPIView):
    """Album List"""
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    # filter_backends = [CustomOrderingFilter]


class AlbumRetrieveAPIView(generics.RetrieveAPIView):
    """Album Retrive"""
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class AlbumUpdateAPIView(generics.UpdateAPIView):
    """Album Updaate"""
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class AlbumDestroyAPIView(generics.DestroyAPIView):
    """Album Delete"""
    queryset = Album.objects.all()


class TrackCreateAPIView(generics.CreateAPIView):
    """Track Create"""
    serializer_class = TrackCreateSerializer


class TrackListAPIView(generics.ListAPIView):
    """Track List"""
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class TrackRetrieveAPIView(generics.RetrieveAPIView):
    """Track Retrive"""
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class TrackUpdateAPIView(generics.UpdateAPIView):
    """Track Updaate"""
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class TrackDestroyAPIView(generics.DestroyAPIView):
    """Track Delete"""
    queryset = Track.objects.all()


class AlbumList(generics.ListAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        queryset = Album.objects.all()
        sorting = self.request.query_params.get('sorting', None)
        if sorting:
            queryset = queryset.order_by(sorting)
        return queryset
