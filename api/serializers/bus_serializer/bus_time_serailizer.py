from rest_framework import serializers

class BusTimeSerializer(serializers.Serializer):
    line = serializers.CharField()
    time = serializers.JSONField()