from rest_framework import serializers

class BusSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    bus_id = serializers.CharField()
    line = serializers.CharField()
    station_id = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    speed = serializers.IntegerField()
