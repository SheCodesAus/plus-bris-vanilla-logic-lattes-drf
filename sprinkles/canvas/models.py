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
    image = models.URLField()

class StickyNote(models.Model):
    title = models.CharField(max_length=200, null=True)
    canvas = models.ForeignKey(
        'Canvas',
        on_delete=models.CASCADE,
        related_name='sticky_notes'
        )
    who = models.TextField(null=True)
    what = models.TextField(null=True)
    why = models.TextField(null=True)
    anonymous = models.BooleanField(default=False)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,default=1)




