import time

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.services.bus_predictions_service import fetch_bus_data, BUS_PREDICTIONS
from api.serializers.bus_serializer import BusSerializer


class BusDataListView(generics.ListAPIView):
    """Non-modify realtime data for mockup frontend."""
    serializer_class = BusSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        data = fetch_bus_data()
        if "error" in data:
            return []
        return data

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LiveBusDataView(generics.ListAPIView):
    """API view to serve live bus data, returning one prediction per bus per request."""
    serializer_class = BusSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """Returns one prediction per bus from the stored predictions."""
        buses_predictions = []

        for bus_id, queue in BUS_PREDICTIONS.items():
            try:
                buses_predictions.append(queue.get(timeout=1))  # Get next prediction for each bus
            except:
                pass  # If no predictions are available, skip this bus

        return buses_predictions  # Return all buses' latest predicted locations

    def list(self, request, *args, **kwargs):
        """Wait 1 second before returning next prediction."""
        time.sleep(1)  # Simulate real-time update every second
        return super().list(request, *args, **kwargs)
