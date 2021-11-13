from django.db import models
from datetime import date

class Canvas(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateField(default=date.today)
    team_name = models.CharField(max_length=200)


class StickyNote(models.Model):
    who = models.CharField(max_length=200)
    what = models.TextField()
    why = models.TextField()
    anonymous = models.BooleanField()
    date_created = models.DateField(default=date.today)

