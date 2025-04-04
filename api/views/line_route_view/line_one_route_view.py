from rest_framework import generics
from rest_framework.permissions import AllowAny
from api.serializers import LineOneRouteSerializer
from api.models import LineOneRoute
import logging

logger = logging.getLogger(__name__)


class LineOneRouteView(generics.ListAPIView):
    serializer_class = LineOneRouteSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        bus_location = LineOneRoute.objects.all()
        logger.info(f"Line One Route data retrieved: {bus_location}")
        return bus_location