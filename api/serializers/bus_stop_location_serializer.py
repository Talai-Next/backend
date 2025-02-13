from ..models import BusLocation
from rest_framework import serializers


class BusStopLocationSerializer(serializers.ModelSerializer):
    """Serializer for get bus stop location."""

    class Meta:
        model = BusLocation
        fields = "__all__"
        extra_kwargs = {"author": {"read_only": True}}
