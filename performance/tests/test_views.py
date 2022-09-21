from django.test import TestCase, Client
from django.urls import reverse, resolve
from performance import views

# Create your tests here.


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.random_revenue_url = reverse("performance:RandomRevenueView")
        self.slow_iteration_url = reverse("performance:SlowIterationView")

    def test_random_revenue_view(self):
        response = self.client.get(self.random_revenue_url)
        self.assertEqual(response.status_code, 200)

    def test_slow_iteration_view(self):
        response = self.client.get(self.slow_iteration_url)
        self.assertEqual(response.status_code, 200)
