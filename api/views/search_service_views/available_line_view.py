from rest_framework import status
from rest_framework.views import APIView
from ...models import StationLocation, LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute
from rest_framework.response import Response
import math

class AvailableLineView(APIView):
    """ Find Available line of current station"""
    def get(self,request):
        try:
            cur = float(request.query_params.get('cur'))
            if cur is None:
                return Response({'error': 'current station is require'}, status=status.HTTP_400_BAD_REQUEST)

            line_routes = {
                "1": LineOneRoute,
                "3": LineThreeRoute,
                "5": LineFiveRoute,
                "s": LineSpecialRoute
            }
            available_lines = [
                line for line, model in line_routes.items() if model.objects.filter(station__id=cur).exists()
            ]
            return Response(available_lines)
        except ValueError:
            return Response({'error': 'Invalid station ID'}, status=status.HTTP_400_BAD_REQUEST)
