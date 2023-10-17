from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Album, Artist, Track


class AlbumListViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.artist = Artist.objects.create(id=1, name='Test Artist')
        self.album = Album.objects.create(
            id=1, name='Test Album', artist=self.artist, year=2001)
        self.track = Track.objects.create(
            id=1, album=self.album, name="Test track"
        )

    def test_album_list(self):
        url = reverse('app:album_list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_artist_list(self):
        url = reverse('app:artist_list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_track_list(self):
        url = reverse('app:track_list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_artist_str(self):
        url = reverse('app:artist_detail', args=[1])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        if isinstance(response.data['name'], str):
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.fail("Значение не строка")

    def test_album_str(self):
        url = reverse('app:album_detail', args=[1])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        if isinstance(response.data['name'], str):
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.fail("Значение не строка")

    def test_album_int(self):
        url = reverse('app:album_detail', args=[1])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        if isinstance(response.data['year'], int):
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.fail("Значение не число")

    def test_track_str(self):
        url = reverse('app:album_detail', args=[1])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        if isinstance(response.data['name'], str):
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.fail("Значение не строка")

    def test_delete_album(self):
        url = reverse('app:album_delete', args=[1])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_artist(self):
        url = reverse('app:artist_delete', args=[1])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_track(self):
        url = reverse('app:track_delete', args=[1])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
