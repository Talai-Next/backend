from rest_framework import status
from rest_framework.views import APIView
from ...models import StationLocation, LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute
from rest_framework.response import Response
from ...services import find_available_line

class AvailableLineView(APIView):
    """ Find Available line of current station"""
    def get(self,request):
        try:
            cur = float(request.query_params.get('cur'))
            if cur is None:
                return Response({'error': 'current station is require'}, status=status.HTTP_400_BAD_REQUEST)

            available_lines = find_available_line(cur)
            return Response(available_lines)
        except ValueError:
            return Response({'error': 'Invalid station ID'}, status=status.HTTP_400_BAD_REQUEST)
