from django.db import models
from django.utils import timezone


# Create your models here.


class MovieShow(models.Model):
    """Model class for Movie and show"""
    type = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    director = models.CharField(max_length=300, blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    date_added = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    listed_in = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
