from ..models import LineFiveRoute
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from .bus_stop_location_serializer import BusStopLocationSerializer


class LineFiveRouteSerializer(serializers.ModelSerializer):
    station = BusStopLocationSerializer()
    permission_classes = [AllowAny]
    class Meta:
        model = LineFiveRoute
        fields = ['id', 'order', 'station']