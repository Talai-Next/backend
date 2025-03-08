from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from ..serializers import LineOneRouteSerializer
from ..models import LineOneRoute


class LineOneRouteView(generics.ListAPIView):
    serializer_class = LineOneRouteSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        bus_location = LineOneRoute.objects.all()
        return bus_location