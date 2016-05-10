from __future__ import unicode_literals
from django.db import models


class Candidate(models.Model):
    CANDIDATE_CATEGORIES = (
        ("SPL", "School Pupil Leader"),
        ("ASPL", "Assistant School Pupil Leader"),
    )
    name = models.CharField(max_length=256)
    description = models.TextField()
    # photo = models.ImageField(upload_to='assets/', default='assets/none.jpg')
    votes = models.IntegerField(default=0)
    category = models.CharField(max_length=4, choices=CANDIDATE_CATEGORIES, default="SPL")
    def __unicode__(self):
        return self.name

