# serializers.py
from rest_framework import serializers

class BusDetailSerializer(serializers.Serializer):
    bus_id = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    station_id = serializers.IntegerField()
    line = serializers.CharField()
