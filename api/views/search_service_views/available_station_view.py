from rest_framework import status
from rest_framework.views import APIView
from ...models import LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute
from rest_framework.response import Response
import math
import requests

from ...serializers import BusStopLocationSerializer


class AvailableStationView(APIView):
    """ Find Available destination station that can reach by current station"""
    def get(self,request):
        try:
            cur = float(request.query_params.get('cur'))
            if cur is None:
                return Response({'error': 'current station is require'}, status=status.HTTP_400_BAD_REQUEST)

            api_url = "http://localhost:8000/api/search/available-line/"
            params = {
                "cur": cur
            }
            response = requests.get(api_url, params=params)
            available_lines = response.json()
            available_stations = set()
            for line in available_lines:
                if line == "1":
                    stations = LineOneRoute.objects.all()
                elif line == "3":
                    stations = LineThreeRoute.objects.all()
                elif line == "5":
                    stations = LineFiveRoute.objects.all()
                else:
                    stations = LineSpecialRoute.objects.all()
                for station in stations:
                    available_stations.add(station.station)
            serializer = BusStopLocationSerializer(list(available_stations), many=True)
            return Response(serializer.data)

        except ValueError:
            return Response({'error': 'Invalid station ID'}, status=status.HTTP_400_BAD_REQUEST)

