from django.db import models
from django.contrib.auth.models import User

class PartyUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(null=False)

