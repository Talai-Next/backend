from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.services import find_available_line
import logging

logger = logging.getLogger(__name__)

class AvailableLineView(APIView):
    """ Find Available line of current station"""
    def get(self,request):
        try:
            cur = float(request.query_params.get('cur'))
            if cur is None:
                return Response({'error': 'current station is require'}, status=status.HTTP_400_BAD_REQUEST)

            available_lines = find_available_line(cur)
            if not available_lines:
                logger.error(f"No available lines found for station ID: {cur}")
                return Response({'error': 'No available lines found'}, status=status.HTTP_404_NOT_FOUND)
            logger.info(f"Available lines found for station ID {cur}: {available_lines}")
            return Response(available_lines)
        except ValueError:
            logger.error(f"Invalid station ID: {request.query_params.get('cur')}")
            return Response({'error': 'Invalid station ID'}, status=status.HTTP_400_BAD_REQUEST)
