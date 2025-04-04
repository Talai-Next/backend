from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.serializers import LineSpecialRouteSerializer
from api.models import LineSpecialRoute
import logging

logger = logging.getLogger(__name__)


class LineSpecialRouteView(generics.ListAPIView):
    serializer_class = LineSpecialRouteSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        bus_location = LineSpecialRoute.objects.all().order_by('order')
        logger.info(f"Line Special Route data retrieved: {bus_location}")
        return bus_location