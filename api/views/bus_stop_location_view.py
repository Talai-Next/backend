from rest_framework import generics
from api.serializers import BusStopLocationSerializer
from rest_framework.permissions import AllowAny
from api.models import StationLocation
import logging

logger = logging.getLogger(__name__)


class BusStopLocationView(generics.ListAPIView):
    serializer_class = BusStopLocationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        bus_location = StationLocation.objects.all()
        logger.info(f"Bus stop locations retrieved: {bus_location}")
        return bus_location
