
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from app.apps import ArtistConfig
from app.views import ArtistCreateAPIView, ArtistListAPIView, ArtistUpdateAPIView, ArtistRetrieveAPIView, \
    ArtistDestroyAPIView, AlbumCreateAPIView, AlbumListAPIView, AlbumRetrieveAPIView, AlbumUpdateAPIView, \
    AlbumDestroyAPIView, TrackCreateAPIView, TrackListAPIView, TrackRetrieveAPIView, TrackUpdateAPIView, \
    TrackDestroyAPIView, AlbumList

app_name = ArtistConfig.name

router = DefaultRouter()

urlpatterns = [
    # Artist
    path(
        "artist/create/",
        ArtistCreateAPIView.as_view(),
        name="artist_create"),
    path("artist/", ArtistListAPIView.as_view(), name="artist_list"),
    path(
        "artist/detail/<int:pk>/",
        ArtistRetrieveAPIView.as_view(),
        name="artist_detail"),
    path(
        "artist/update/<int:pk>/",
        ArtistUpdateAPIView.as_view(),
        name="artist_update"),
    path(
        "artist/delete/<int:pk>/",
        ArtistDestroyAPIView.as_view(),
        name="artist_delete"),
    # Album
    path("album/create/", AlbumCreateAPIView.as_view(), name="album_create"),
    path("album/", AlbumListAPIView.as_view(), name="album_list"),
    path(
        "album/detail/<int:pk>/",
        AlbumRetrieveAPIView.as_view(),
        name="album_detail"),
    path(
        "album/update/<int:pk>/",
        AlbumUpdateAPIView.as_view(),
        name="album_update"),
    path(
        "album/delete/<int:pk>/",
        AlbumDestroyAPIView.as_view(),
        name="album_delete"),
    #  Track
    path("track/create/", TrackCreateAPIView.as_view(), name="track_create"),
    path("track/", TrackListAPIView.as_view(), name="track_list"),
    path(
        "track/detail/<int:pk>/",
        TrackRetrieveAPIView.as_view(),
        name="track_detail"),
    path(
        "track/update/<int:pk>/",
        TrackUpdateAPIView.as_view(),
        name="track_update"),
    path(
        "track/delete/<int:pk>/",
        TrackDestroyAPIView.as_view(),
        name="track_delete"),
    # Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # All_info
    path('albums/', AlbumList.as_view(), name='albums-list')
] + router.urls
