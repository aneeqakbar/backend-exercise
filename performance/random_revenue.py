import random
from django.db.models import F
from performance.models import DailyPerformance


def random_revenue():
    data = DailyPerformance.objects.filter_by_min_roi(50)
    print("length: ", data.count())
    print("length x2: ", data.count() * 2)
    for index, item in enumerate(data, 0):
        print(f"{index+1}/{data.count()}")
        item.revenue = F("revenue") * random.uniform(0.5, 2)
    DailyPerformance.objects.bulk_update(data, fields=["revenue"])
