from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Medicine1(models.Model):
    Person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Days = models.IntegerField()
    Description = models.CharField(max_length=100)
    Times = models.IntegerField()
