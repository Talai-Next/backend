from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.services import passenger_density_prediction
import logging

logger = logging.getLogger(__name__)

class DensityView(APIView):
    def post(self, request, *args, **kwargs):
        bus_id = request.data.get("bus_id")
        line = request.data.get("line")
        try:
            predicted_density = passenger_density_prediction(bus_id)
            logger.info(f"Predicted density for bus ID {bus_id}: {predicted_density}")
            return Response({
                "bus_id": bus_id,
                "line": line,
                "predicted_density": predicted_density
            }, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error occurred while predicting passenger density: {str(e)}")
            return Response({
                "error": "Failed to predict passenger density"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        