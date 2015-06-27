__author__ = 'emillykarungi'

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()

    def __unicode__(self):
        return self.title
