import time
import logging

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.services import fetch_bus_data, get_predictions
from api.serializers import BusLocationSerializer

logger = logging.getLogger(__name__)


class MockupBusesLocationListView(generics.ListAPIView):
    """Non-modify realtime data for mockup frontend."""
    serializer_class = BusLocationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        data = fetch_bus_data()
        if "error" in data:
            return []
        logger.info(f"Mockup bus location data: {data}")
        return data

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        logger.info(f"Mockup bus location data serialized: {serializer.data}")
        return Response(serializer.data)


class PredictedBusDataView(generics.ListAPIView):
    """API view to serve predicted bus data, returning one prediction per bus per request."""
    serializer_class = BusLocationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """Returns one prediction per bus from the stored predictions."""
        buses_predictions = []
        bus_location_predictions = get_predictions()

        for bus_id, queue in bus_location_predictions.items():
            try:
                buses_predictions.append(queue.get(timeout=1))  # Get next prediction for each bus
            except:
                pass  # If no predictions are available, skip this bus
        
        logger.info(f"Predicted bus data: {buses_predictions}")
        return buses_predictions  # Return all buses' latest predicted locations

    def list(self, request, *args, **kwargs):
        """Wait 1 second before returning next prediction."""
        time.sleep(1)  # Simulate real-time update every second
        logger.info("Waiting for 1 second before returning next prediction.")
        return super().list(request, *args, **kwargs)
