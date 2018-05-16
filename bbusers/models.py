from django.db import models


class BbUser(models.Model):
  firstName = models.CharField(max_length=40)
  lastName = models.CharField(max_length=50)
  email = models.CharField(max_length=75)
  username = models.CharField(max_length=75)
