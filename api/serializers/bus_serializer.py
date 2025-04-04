from rest_framework import serializers

class BusSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    bus_id = serializers.CharField()
    line = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    speed = serializers.IntegerField()
