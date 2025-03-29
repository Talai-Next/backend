from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import BusDetailSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ..services.bus_detail_service  import BUS_LOCATIONS  # Import the BUS_LOCATIONS dictionary

@method_decorator(csrf_exempt, name='dispatch')
class BusDetailView(APIView):
    """
    API endpoint that returns bus's detail include station and estimate time.
    """
    def get(self, request):
        bus_locations = BUS_LOCATIONS
        # Serialize the bus location data
        data = []
        for bus_id, location in bus_locations.items():
            data.append({
                'bus_id': bus_id,
                'latitude': location['latitude'],
                'longitude': location['longitude'],
                'station_id': location['station_id']
            })
        serializer = BusDetailSerializer(list(data), many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

