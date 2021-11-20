from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

class Canvas(models.Model):
    team = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_public = models.BooleanField()
    date_created = models.DateField(default=date.today)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)

class StickyNote(models.Model):
    title = models.CharField(max_length=200)
    canvas = models.ForeignKey(
        'Canvas',
        on_delete=models.CASCADE,
        related_name='sticky_notes'
        )
    who = models.TextField()
    what = models.TextField()
    why = models.TextField()
    anonymous = models.BooleanField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,default=1)




