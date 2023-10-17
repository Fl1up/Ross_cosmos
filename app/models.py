from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255, verbose_name="Артист")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=255, verbose_name="Альбом")
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        verbose_name="Артист")
    year = models.PositiveIntegerField(verbose_name="Год")

    def __str__(self):
        return f"{self.name}[{self.year}]"

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


class Track(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        verbose_name="Альбом")
    name = models.CharField(max_length=255, verbose_name="Трек")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Трек"
        verbose_name_plural = "Треки"
