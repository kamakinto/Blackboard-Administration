from django.db import models
from django.conf import settings
# Create your models here.

class UserProfile(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
  nickname = models.CharField(max_length=30)
  photo = models.ImageField(upload_to='profile_pics/')
  job_title = models.CharField(max_length=50)
  extension = models.IntegerField()
  bio = models.TextField()
  cohort = (
    ('faculty', 'Faculty'),
    ('staff', 'Staff'),
    ('student', 'Student'),
  )
