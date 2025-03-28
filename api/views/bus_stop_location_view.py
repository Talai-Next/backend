import requests
from rest_framework import generics
from ..serializers import BusStopLocationSerializer
from rest_framework.permissions import AllowAny
from ..models import StationLocation
from django.http import JsonResponse


def proxy_buses(request):
    try:
        response = requests.get("http://localhost:8080/api/buses/")
        response.raise_for_status()
        return JsonResponse(response.json(), safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)


class BusStopLocationView(generics.ListAPIView):
    serializer_class = BusStopLocationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        bus_location = StationLocation.objects.all()
        return bus_location
