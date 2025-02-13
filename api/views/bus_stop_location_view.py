from rest_framework import generics
from ..serializers import BusStopLocationSerializer
from rest_framework.permissions import AllowAny
from ..models import BusLocation


class BusStopLocationView(generics.ListAPIView):
    serializer_class = BusStopLocationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        bus_location = BusLocation.objects.all()
        return bus_location
