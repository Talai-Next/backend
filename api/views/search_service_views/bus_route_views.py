from rest_framework import status
from rest_framework.views import APIView
from ...models import LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute, StationLocation
from rest_framework.response import Response
import math
import requests

class BusRouteView(APIView):
    """
        Find Bus Route that user has to use
    """
    def get(self, request):
        try:
            cur_id = request.query_params.get('cur')
            des_id = request.query_params.get('des')

            line = self.find_shortest_line(cur_id,des_id)
            return Response({line})
        except ValueError:
            return Response({'error': 'Invalid station ID'}, status=status.HTTP_400_BAD_REQUEST)

    def get_avalable_line(self, cur_id, des_id):
        api_url = "http://localhost:8000/api/search/available-line/"
        cur_params = {"cur": cur_id}
        des_params = {"cur": des_id}

        try:
            cur_response = requests.get(api_url, params=cur_params)
            des_response = requests.get(api_url, params=des_params)

            if cur_response.status_code != 200 or des_response.status_code != 200:
                raise ValueError("Failed to fetch available lines from the API")

            cur_line = set(cur_response.json())
            des_line = set(des_response.json())
            print(cur_line)
            print(des_line)
            available_line = cur_line.intersection(des_line)
            print(available_line)
            return available_line

        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {e}")

    def find_shortest_line(self, cur_id, des_id):
        """ Find the shortest path"""
        line_routes = {
            "1": LineOneRoute,
            "3": LineThreeRoute,
            "5": LineFiveRoute,
            "s": LineSpecialRoute
        }
        min_distance = float('inf')
        distance = 0
        shortest_line = ""
        available_line = self.get_avalable_line(cur_id, des_id)
        for line in available_line:
            cur_order = line_routes[line].objects.get(station__id=cur_id).order
            des_order = line_routes[line].objects.get(station__id=des_id).order

            if des_order >= cur_order:
                distance = des_order - cur_order
            else:
                all_station = line_routes[line].objects.count()
                distance = all_station - ((cur_order - des_order) + 1)

            if distance < min_distance:
                min_distance = distance
                shortest_line = line
        return shortest_line


