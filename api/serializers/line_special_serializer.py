from ..models import LineSpecialRoute
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from .bus_stop_location_serializer import BusStopLocationSerializer


class LineSpecialRouteSerializer(serializers.ModelSerializer):
    station = BusStopLocationSerializer()
    permission_classes = [AllowAny]
    class Meta:
        model = LineSpecialRoute
        fields = ['id', 'order', 'station']