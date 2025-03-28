from rest_framework import status
from rest_framework.views import APIView
from ...models import LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute
from rest_framework.response import Response
import requests
from ...services import available_station
from ...serializers import BusStopLocationSerializer


class AvailableStationView(APIView):
    """ Find Available destination station that can reach by current station"""
    def get(self,request):
        try:
            cur = float(request.query_params.get('cur'))
            if cur is None:
                return Response({'error': 'current station is require'}, status=status.HTTP_400_BAD_REQUEST)

            available_stations = available_station(cur)
            serializer = BusStopLocationSerializer(list(available_stations), many=True)
            return Response(serializer.data)

        except ValueError:
            return Response({'error': 'Invalid station ID'}, status=status.HTTP_400_BAD_REQUEST)

