from rest_framework.response import Response
from rest_framework.views import APIView
from performance.tasks import slow_iteration
from .random_revenue import random_revenue

# Create your views here.


class RandomRevenueView(APIView):
    def get(self, request):
        data = random_revenue()
        return Response(status=200)


class SlowIterationView(APIView):
    def get(self, request):
        slow_iteration.delay()
        return Response(status=200)
