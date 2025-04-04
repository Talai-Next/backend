from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...serializers import BusSerializer
from django.http import JsonResponse
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
        for obj_id, location in bus_locations.items():
            data.append({
                'id': obj_id,
                'bus_id': location['bus_id'],
                'latitude': location['latitude'],
                'line': location['line'],
            })
        serializer = BusSerializer(list(data), many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

