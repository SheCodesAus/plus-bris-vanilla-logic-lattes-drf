from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

class Canvas(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateField(default=date.today)
    team = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)


