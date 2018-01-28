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
    location = models.CharField(max_length=200)
    placeId = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.location

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.location)[:50]

        return super(Map, self).save(*args, **kwargs)
