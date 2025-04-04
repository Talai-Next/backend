from rest_framework import serializers


class BusNextStationSerializer(serializers.Serializer):
    bus_id = serializers.CharField()
    station_id = serializers.CharField()
    order = serializers.IntegerField()
    line = serializers.CharField()
