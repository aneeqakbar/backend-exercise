from rest_framework import serializers

from performance.models import DailyPerformance


class DailyPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPerformance
        fields = "__all__"
