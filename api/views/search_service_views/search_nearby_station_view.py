from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ...services import find_nearest_station, find_nearest_accessible_station
import logging

logger = logging.getLogger(__name__)

class SearchNearbyStationView(APIView):
    """Search the nearest station to user location depend on their destination station """

    def get(self,request):
        try:
            lat = float(request.query_params.get('lat'))
            lon = float(request.query_params.get('lon'))
            des_id = request.query_params.get('des_id')
            if lat is None or lon is None:
                return Response({'error': 'latitude and longitude are required'}, status=status.HTTP_400_BAD_REQUEST)
            if des_id is None:
                nearest_station = find_nearest_station(lat, lon)
            else:
                nearest_station= find_nearest_accessible_station(lat, lon, des_id)
            if nearest_station:
                logger.info(f"Nearest station found: {nearest_station}")
                return Response({
                    'id': nearest_station.id,
                    'station_code': nearest_station.station_code,
                    'name': nearest_station.name,
                    'latitude': nearest_station.latitude,
                    'longitude': nearest_station.longitude,
                })
            
        except ValueError:
            logger.error(f"Invalid latitude or longitude: {request.query_params.get('lat')}, {request.query_params.get('lon')}")
            return Response({'error': 'Invalid latitude or longitude.'}, status=status.HTTP_400_BAD_REQUEST)

