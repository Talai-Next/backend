from rest_framework import serializers

class BusSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    line = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    speed = serializers.IntegerField()
