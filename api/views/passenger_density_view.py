# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import passenger_density_prediction

class DensityView(APIView):
    def post(self, request, *args, **kwargs):
        bus_id = request.data.get("bus_id")
        line = request.data.get("line")
        predicted_density = passenger_density_prediction(bus_id)

        return Response({
            "bus_id": bus_id,
            "line": line,
            "predicted_density": predicted_density
        }, status=status.HTTP_200_OK)
