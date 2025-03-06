from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from ..serializers import LineFiveRouteSerializer
from ..models import LineFiveRoute


class LineFiveRouteView(generics.ListAPIView):
    serializer_class = LineFiveRouteSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        bus_location = LineFiveRoute.objects.all()
        return bus_location