from rest_framework import  generics
from rest_framework.permissions import AllowAny

from ..serializers import ObstacleMarkerSerializer
from ..models import ObstaclePosition


class ObstacleMarkerView(generics.ListAPIView):
    serializer_class = ObstacleMarkerSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        obstacle_type = self.kwargs.get('obstacle_type')
        return ObstaclePosition.objects.filter(obstacle_type=obstacle_type)

