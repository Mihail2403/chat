from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Message(models.Model):
    text = models.TextField()
