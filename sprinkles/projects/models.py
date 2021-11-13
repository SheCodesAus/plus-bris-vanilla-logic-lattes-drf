from django.db import models
from datetime import date

class Canvas(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateField(default=date.today)
    team = models.CharField(max_length=200)


