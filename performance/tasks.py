import time
from celery import shared_task

from performance.models import DailyPerformance


@shared_task
def slow_iteration():
    queryset = DailyPerformance.objects.all()[:50]
    for item in queryset:
        print(item.id)
        time.sleep(60)
    return None
