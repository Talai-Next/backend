from rest_framework import serializers
from .models import LineOneRoute, LineTwoRoute
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from .models import BusLocation

class BusLocationSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]
    class Meta:
        model = BusLocation
        fields = ['id', 'station_code', 'name', 'latitude', 'longitude']

class LineOneRouteSerializer(serializers.ModelSerializer):
    station =  BusLocationSerializer()
    permission_classes = [AllowAny]
    class Meta:
        model = LineOneRoute
        fields = ['id', 'order', 'station']
