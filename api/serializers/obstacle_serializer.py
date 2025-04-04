from api.models import ObstaclePosition
from rest_framework.permissions import AllowAny
from rest_framework import serializers


class ObstacleMarkerSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]

    class Meta:
        model = ObstaclePosition
        fields = '__all__'
