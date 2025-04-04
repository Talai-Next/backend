from rest_framework import status
from rest_framework.views import APIView
from ...models import LineOneRoute, LineThreeRoute, LineFiveRoute, LineSpecialRoute, StationLocation
from rest_framework.response import Response
from ...services import find_bus_route
class BusRouteView(APIView):
    """ Find Bus Route that user has to use """
    def get(self, request):
        try:
            cur_id = request.query_params.get('cur')
            des_id = request.query_params.get('des')
            line = find_bus_route(cur_id,des_id)
            return Response({line})
        except ValueError:
            return Response({'error': 'Invalid station ID'}, status=status.HTTP_400_BAD_REQUEST)

