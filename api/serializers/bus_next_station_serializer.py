from rest_framework import serializers

class BusSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    bus_id = serializers.CharField()
    line = serializers.CharField()
    station_id = serializers.CharField()
