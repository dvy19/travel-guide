import os

from celery import Celery

# Tell Celery which Django settings file to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "travel_project.settings")

# Create Celery application
app = Celery("travel_project")

# Read configuration from Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Automatically discover tasks.py from installed apps
app.autodiscover_tasks()