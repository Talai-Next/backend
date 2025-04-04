from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ...services import find_bus_route
import logging

logger = logging.getLogger(__name__)

class BusRouteView(APIView):
    """ Find Bus Route that user has to use """
    def get(self, request):
        try:
            cur_id = request.query_params.get('cur')
            des_id = request.query_params.get('des')
            line = find_bus_route(cur_id,des_id)
            if not line:
                logger.error(f"No bus route found from station ID {cur_id} to {des_id}")
                return Response({'error': 'No bus route found'}, status=status.HTTP_404_NOT_FOUND)
            logger.info(f"Bus route found from station ID {cur_id} to {des_id}: {line}")
            return Response({line})
        except ValueError:
            logger.error(f"Invalid station ID: {request.query_params.get('cur')}")
            return Response({'error': 'Invalid station ID'}, status=status.HTTP_400_BAD_REQUEST)

