# -*- coding: utf-8 -*-
# from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Map(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # pub_date = models.DateTimeField(default=now)
    # title = models.CharField(max_length=200)
    # slug = models.SlugField(null=True, blank=True)
    # body = models.TextField()
    place_id = models.TextField(max_length=700, null=True)
    address = models.TextField(max_length=200, null=True)
    rating = models.FloatField(default=0.0)
    # overall_reviews = models.ForeignKey()

    def __unicode__(self):
        return self.location

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.location)[:50]

        return super(Map, self).save(*args, **kwargs)


class Reviews(models.Model):
    place_id = models.ForeignKey(Map)
    reviews = models.TextField(max_length=1000, null=True)
    rating = models.FloatField(default=0.0)
    user_locations = models.TextField(max_length=200, null=True)
    sentiment = models.FloatField(default=0.0)
    time = models.TimeField(null=True)


    def __unicode__(self):
        return self.location

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.reviews)[:50]

        return super(Reviews, self).save(*args, **kwargs)
