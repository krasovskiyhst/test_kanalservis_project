import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_kanalservis_project.settings')

app = Celery('spreadsheet_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get_and_write_an_order_in_the_database': {
        'task': 'spreadsheet_app.logic.tasks.get_and_write_an_order_in_the_database',
        'schedule': crontab(minute='*/1'),
    },
}
