import os
from celery import Celery, shared_task
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=10, hour=0),
        run_once_a_day.s('once a day')
    )
    sender.add_periodic_task(
        crontab(minute=0, hour='*/6'),
        run_six_times_a_day.s('six daily task')
    )
    sender.add_periodic_task(
        crontab(minute=0, hour=1, day_of_month=1),
        run_every_month.s('every_month')
    )


@shared_task
def run_once_a_day(name):
    """ Tasks for run once a day """
    pass


@shared_task
def run_six_times_a_day(name):
    """ Tasks for run six times a day """
    pass


@shared_task
def run_every_month(name):
    """ Tasks for run one in month """
    pass
