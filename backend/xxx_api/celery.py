import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poc_background_mq.settings")

app = Celery("poc_background_mq")

app.config_from_object("django.conf.settings", namespace="CELERY")
app.autodiscover_tasks()
