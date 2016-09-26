from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    text = models.TextField()

    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

    def get_absolute_url(self):
        return "/news/%i/" % self.id


class NewsImage(models.Model):
    news = models.ForeignKey(News)
    image = models.ImageField(upload_to='post/images')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.id)
