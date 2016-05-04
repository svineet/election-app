from __future__ import unicode_literals
from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    # photo = models.ImageField(upload_to='assets/', default='assets/none.jpg')
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

