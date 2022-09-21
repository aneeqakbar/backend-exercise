from django.test import TestCase
from performance.models import DailyPerformance

# Create your tests here.


class TestModels(TestCase):
    def setUp(self):
        self.daily_performence1 = DailyPerformance.objects.create(cost=10, revenue=5)
        self.daily_performence2 = DailyPerformance.objects.create(cost=10, revenue=2)
        self.daily_performence3 = DailyPerformance.objects.create(cost=10, revenue=2)

    def test_filter_by_min_roi(self):
        filter_by_80 = DailyPerformance.objects.filter_by_min_roi(80)
        filter_by_50 = DailyPerformance.objects.filter_by_min_roi(50)
        filter_by_20 = DailyPerformance.objects.filter_by_min_roi(20)

        self.assertEqual(filter_by_80.count(), 0)
        self.assertEqual(filter_by_50.count(), 1)
        self.assertEqual(filter_by_20.count(), 3)

    def test_get_roi_property(self):
        self.assertEqual(self.daily_performence1.get_roi, float(50))
        self.assertEqual(self.daily_performence2.get_roi, float(20))
        self.assertEqual(self.daily_performence3.get_roi, float(20))
