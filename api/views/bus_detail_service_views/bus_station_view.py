from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...serializers import BusNextStationSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ...services.bus_detail_service import BUS_NEXT_STATION  # Import the BUS_LOCATIONS dictionary

@method_decorator(csrf_exempt, name='dispatch')
class BusLocationView(APIView):
    """
    API endpoint that returns bus's closest station
    """
    def get(self, request):
        bus_locations = BUS_NEXT_STATION
        # Serialize the bus location data
        data = []
        for obj_id, detail in bus_locations.items():
            data.append({
                'id': obj_id,
                'bus_id': detail['bus_id'],
                'station_id': detail['station_id'],
                'order': detail['order'],
                'line': detail['line'],
            })
        serializer = BusNextStationSerializer(list(data), many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

