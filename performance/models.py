from django.db import models
from django.db.models import F, ExpressionWrapper

# Create your models here.


class PerformanceManager(models.Manager):
    def filter_by_min_roi(self, min_roi: float):
        return (
            self.annotate(
                quotient=ExpressionWrapper(
                    F("revenue") * 100 / F("cost") * 100, models.FloatField()
                )
            )
            .annotate(
                min_roi=ExpressionWrapper(
                    F("quotient") / 100, output_field=models.FloatField()
                )
            )
            .filter(min_roi__gte=min_roi)
        )


class Performance(models.Model):
    cost = models.IntegerField(default=0)
    revenue = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = PerformanceManager()

    class Meta:
        abstract = True

    @property
    def get_roi(self):
        return float(self.revenue / self.cost * 100)


class DailyPerformance(Performance):
    date = models.DateField(auto_now_add=True)


class HourlyPerformance(Performance):
    datetime = models.DateTimeField(auto_now_add=True)
