from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Actor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    class Meta:
        ordering = ("firstname",)
        verbose_name_plural = "actors"

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "cinemahalls"

    def __str__(self):
        places = int(self.rows) * int(self.seats_in_row)
        return f"{self.name} - {places}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    duration = models.IntegerField()

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title
