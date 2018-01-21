from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
 
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodlunch.settings')

app = Celery('foodlunch')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)
# Time Zone
app.conf.timezone = 'America/Santiago'

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# Periodic Task configuration
# http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#solar-schedules
app.conf.beat_schedule = {
    'send-report-menu-today': {
        'task': 'lunch.tasks.task_mail',
        'schedule': crontab(minute=30, hour=8),  # change to `crontab(minute=0, hour=0)` crontab(minute=3, hour=15, day_of_week='1-6') if you want it to run daily at midnight
    },
}
