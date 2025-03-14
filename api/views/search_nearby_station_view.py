from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from ..serializers import LineSpecialRouteSerializer
from ..models import StationLocation, LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute
from rest_framework.response import Response
import math

class SearchNearbyStationView(APIView):
    line1 = LineOneRoute.objects.all()
    line3 = LineThreeRoute.objects.all()
    line5 = LineFiveRoute.objects.all()
    lineS = LineSpecialRoute.objects.all()
    station = StationLocation.objects.all()

    def get(self,request):
        try:
            lat = float(request.query_params.get('lat'))
            lon = float(request.query_params.get('lon'))
            des_id = request.query_params.get('des_id')
            if lat is None or lon is None:
                return Response({'error': 'latitude and longitude are required'}, status=status.HTTP_400_BAD_REQUEST)
            if des_id is None:
                nearest_station = self.find_nearest_station(lat, lon)
                line = None
            else:
                nearest_station, line = self.find_nearest_accessible_station(lat, lon, des_id)
            if nearest_station:
                return Response({
                    'id': nearest_station.id,
                    'station_code': nearest_station.station_code,
                    'name': nearest_station.name,
                    'latitude': nearest_station.latitude,
                    'longitude': nearest_station.longitude,
                    'line': line
                })
        except ValueError:
            return Response({'error': 'Invalid latitude or longitude.'}, status=status.HTTP_400_BAD_REQUEST)

    def find_distance(self, lat1, lon1, lat2, lon2):
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

    def find_nearest_station(self,lat,lon):
        """ Find nearest station"""
        min_distance = float("inf")
        nearest_station = None
        for i in SearchNearbyStationView.station:
            distance = (self.find_distance(i.latitude,i.longitude,lat,lon))
            if distance < min_distance:
                min_distance = distance
                nearest_station = i
        return nearest_station

    def find_nearest_station_line(self,lat,lon,line):
        """ Find nearest station"""
        min_distance = float("inf")
        nearest_station = None
        for i in line:
            distance = (self.find_distance(i.station.latitude,i.station.longitude,lat,lon))
            if distance < min_distance:
                min_distance = distance
                nearest_station = i.station
        return nearest_station

    def find_nearest_accessible_station(self,lat,lon,des):
        """ Find the nearest station that can reach destination station"""
        one = LineOneRoute.objects.filter(station__id=des).exists()
        three = LineThreeRoute.objects.filter(station__id=des).exists()
        five = LineFiveRoute.objects.filter(station__id=des).exists()
        special = LineSpecialRoute.objects.filter(station__id=des).exists()

        existed = {"1": one,"3": three,"5": five,"s": special}
        line_queries = {"1": SearchNearbyStationView.line1 ,"3": SearchNearbyStationView.line3,"5": SearchNearbyStationView.line5,"s": SearchNearbyStationView.lineS}
        nearest = {}
        min_distance = float('inf')
        nearest_line = ""
        for line, is_exist in existed.items():
            if is_exist:
                stations = line_queries[line]
                nearest_station = self.find_nearest_station_line(lat, lon, stations)

                nearest[line] = nearest_station
                distance = self.find_distance(lat, lon, nearest_station.latitude,nearest_station.longitude)
                if distance < min_distance:
                    min_distance = distance
                    nearest_line = line
        return nearest[nearest_line], nearest_line

