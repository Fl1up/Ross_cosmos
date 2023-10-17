from rest_framework import serializers, filters
from rest_framework.response import Response

from app.models import Artist, Album, Track


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name',)


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('name',)


class AlbumSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name')
    track_set = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ('name', 'artist_name', 'year', 'track_set')


class ArtistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

    def create(self, validated_data):
        artist_item = Artist.objects.create(**validated_data)
        return artist_item


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

    def create(self, validated_data):
        album_item = Album.objects.create(**validated_data)
        return album_item


class TrackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"

    def create(self, validated_data):
        track_item = Track.objects.create(**validated_data)
        return track_item
