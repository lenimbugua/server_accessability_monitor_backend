import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'network_stats.settings')

app = Celery('network_stats')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
