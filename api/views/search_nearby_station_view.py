from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from ..serializers import LineSpecialRouteSerializer
from ..models import StationLocation
from rest_framework.response import Response
import math

class SearchNearbyStationView(APIView):
    def get(self,request):
        try:
            lat = float(request.query_params.get('lat'))
            lon = float(request.query_params.get('lon'))
            if lat is None or lon is None:
                return Response({'error': 'latitude and longitude are required'}, status=status.HTTP_400_BAD_REQUEST)
            nearest_station = self.find_nearest_station(lat,lon)
            if nearest_station:
                return Response({
                    'id': nearest_station.id,
                    'station_code': nearest_station.station_code,
                    'name': nearest_station.name,
                    'latitude': nearest_station.latitude,
                    'longitude': nearest_station.longitude
                })
        except ValueError:
            return Response({'error': 'Invalid latitude or longitude.'}, status=status.HTTP_400_BAD_REQUEST)

    def find_nearest_station(self,lat,lon):
        """ Find nearest station"""
        station_location = StationLocation.objects.all()
        min_distance = float("inf")
        nearest_station = ""
        for i in station_location:
            distance = (self.find_distance(i.latitude,i.longitude,lat,lon))
            if distance < min_distance:
                min_distance = distance
                nearest_station = i.name
        return StationLocation.objects.get(name=nearest_station)

    def find_distance(self,lat1, lon1, lat2, lon2):
        """ Find distance between 2 place on earth in meter"""
        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        r = 6371
        # Return distance in meters
        return r * c * 1000