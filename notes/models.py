from django.conf import settings
from django.db import models
from django.utils import timezone

class Note(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
