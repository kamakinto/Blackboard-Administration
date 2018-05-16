# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def getUserList():
  return 'testing to see if celery freaking works.'

@shared_task
def uploadUserList(userList):
  pass