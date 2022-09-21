from django.urls import path
from . import views

app_name = "performance"

urlpatterns = [
    path(
        "random-revenue/", views.RandomRevenueView.as_view(), name="RandomRevenueView"
    ),
    path(
        "slow-iteration/", views.SlowIterationView.as_view(), name="SlowIterationView"
    ),
]
