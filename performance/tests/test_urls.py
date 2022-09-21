from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from performance import views

# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_random_revenue_resolves(self):
        url = reverse("performance:RandomRevenueView")
        self.assertEqual(resolve(url).func.view_class, views.RandomRevenueView)

    def test_slow_iteration_resolves(self):
        url = reverse("performance:SlowIterationView")
        self.assertEqual(resolve(url).func.view_class, views.SlowIterationView)
