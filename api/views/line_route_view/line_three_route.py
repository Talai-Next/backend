from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from api.serializers import LineThreeRouteSerializer
from api.models import LineThreeRoute


class LineThreeRouteView(generics.ListAPIView):
    serializer_class = LineThreeRouteSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        bus_location = LineThreeRoute.objects.all()
        return bus_location