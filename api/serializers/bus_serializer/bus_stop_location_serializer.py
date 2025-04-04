from api.models import StationLocation
from rest_framework import serializers


class BusStopLocationSerializer(serializers.ModelSerializer):
    """Serializer for get bus stop location."""

    class Meta:
        model = StationLocation
        fields = "__all__"
