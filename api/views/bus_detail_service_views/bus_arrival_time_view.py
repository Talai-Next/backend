from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from api.services.bus_detail_service import BUS_ARRIVAL_TIME  # Import the BUS_LOCATIONS dictionary
from api.serializers import BusTimeSerializer
import logging

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name='dispatch')
class BusArrivalTimeView(APIView):
    """
    API endpoint that returns bus's detail include station and estimate time.
    """

    def get(self, request):
        arrival_time = BUS_ARRIVAL_TIME
        # Serialize the bus location data
        data = []
        try:
            for bus_id, time in arrival_time.items():
                data.append({
                    'line': time['line'],
                    'time': time['time'],
                })
            serializer = BusTimeSerializer(list(data), many=True)
            logger.info(f"Bus arrival time data: {serializer.data}")
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error occurred while fetching bus arrival time: {str(e)}")
            return JsonResponse({
                "error": "Failed to fetch bus arrival time"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
