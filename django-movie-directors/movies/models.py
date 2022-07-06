from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    birth = models.DateField(null=True, blank=True)
    dead = models.DateField(null=True, blank=True)
    bio = models.TextField()

    image = models.URLField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    resume = models.TextField()
    duration = models.PositiveIntegerField()
    image = models.URLField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name
