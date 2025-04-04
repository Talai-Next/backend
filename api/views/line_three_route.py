from rest_framework import generics
from rest_framework.permissions import AllowAny
from ..serializers import LineThreeRouteSerializer
from ..models import LineThreeRoute
import logging

logger = logging.getLogger(__name__)


class LineThreeRouteView(generics.ListAPIView):
    serializer_class = LineThreeRouteSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        bus_location = LineThreeRoute.objects.all()
        logger.info(f"Line Three Route data retrieved: {bus_location}")
        return bus_location