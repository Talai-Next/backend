from rest_framework import generics
from rest_framework.permissions import AllowAny
from ..serializers import LineFiveRouteSerializer
from ..models import LineFiveRoute
import logging

logger = logging.getLogger(__name__)


class LineFiveRouteView(generics.ListAPIView):
    serializer_class = LineFiveRouteSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        bus_location = LineFiveRoute.objects.all()
        logger.info(f"Line Five Route data retrieved: {bus_location}")
        return bus_location