from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.serializers import ObstacleMarkerSerializer
from api.models import ObstaclePosition
import logging

logger = logging.getLogger(__name__)


class ObstacleMarkerView(generics.ListAPIView):
    serializer_class = ObstacleMarkerSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        obstacle_type = self.kwargs.get('obstacle_type')
        logger.info(f"Obstacle type requested: {obstacle_type}")
        return ObstaclePosition.objects.filter(obstacle_type=obstacle_type)

