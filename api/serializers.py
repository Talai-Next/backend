from rest_framework import serializers
from .models import LineOneRoute, LineTwoRoute

from rest_framework import serializers
from .models import BusLocation

class BusLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusLocation
        fields = ['id', 'station_code', 'name', 'latitude', 'longitude']

class LineOneRouteSerializer(serializers.ModelSerializer):
    station =  BusLocationSerializer()
    class Meta:
        model = LineOneRoute
        fields = ['id', 'order', 'station']
