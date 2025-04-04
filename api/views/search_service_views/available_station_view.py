from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.services import available_station
from api.serializers import BusStopLocationSerializer
import logging

logger = logging.getLogger(__name__)

class AvailableStationView(APIView):
    """ Find Available destination station that can reach by current station"""
    def get(self,request):
        try:
            cur = float(request.query_params.get('cur'))
            if cur is None:
                return Response({'error': 'current station is require'}, status=status.HTTP_400_BAD_REQUEST)

            available_stations = available_station(cur)
            serializer = BusStopLocationSerializer(list(available_stations), many=True)
            logger.info(f"Available stations found for station ID {cur}: {serializer.data}")
            return Response(serializer.data)

        except ValueError:
            logger.error(f"Invalid station ID: {request.query_params.get('cur')}")
            return Response({'error': 'Invalid station ID'}, status=status.HTTP_400_BAD_REQUEST)

