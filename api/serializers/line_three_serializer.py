from ..models import LineThreeRoute
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from .bus_stop_location_serializer import BusStopLocationSerializer


class LineThreeRouteSerializer(serializers.ModelSerializer):
    station = BusStopLocationSerializer()
    permission_classes = [AllowAny]
    class Meta:
        model = LineThreeRoute
        fields = ['id', 'order', 'station']