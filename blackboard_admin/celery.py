from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blackboard_admin.settings')

app = Celery('blackboard_admin')

# Using a strong here means the worker does'nt have to serialize
# the configuration object to child processes.
# - namespace = 'CELERY' means all celery-related configuration keys
# should have a 'CELERY_' prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
  print('Request: {0!r}'.format(self.request))


#execute every hour for pulling in the users and adding them to the django database: crontab(minute=0, hour=' */1')
##execute every hour for pulling in the users and adding them to the django database, then putting them into Blackboard: crontab(minute=0, hour=' */5')

