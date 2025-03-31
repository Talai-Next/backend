import requests
from rest_framework import generics
from ...serializers import BusStopLocationSerializer
from ...models import StationLocation
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SelectStationView(APIView):
    """ response current and destination station data"""
    def get(self, request):
        try:
            cur_id = request.query_params.get('cur')
            des_id = request.query_params.get('des')
            cur_station = StationLocation.objects.get(id=cur_id)
            des_station = StationLocation.objects.get(id=des_id)
            cur_station_data = BusStopLocationSerializer(cur_station).data
            des_station_data = BusStopLocationSerializer(des_station).data

            return Response([cur_station_data, des_station_data], status=status.HTTP_200_OK)

        except ValueError:
            return Response({'error': 'Invalid station ID'}, status=status.HTTP_400_BAD_REQUEST)

