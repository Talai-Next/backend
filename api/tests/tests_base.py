from django.test import TestCase
from api.models import *


class BaseTest(TestCase):
    def setUp(self):
        # Create two stations
        self.station_a = StationLocation.objects.create(
            id=1, name="Station A", latitude=13.736717, longitude=100.523186
        )
        self.station_b = StationLocation.objects.create(
            id=2, name="Station B", latitude=13.738000, longitude=100.524000
        )
        self.station_c = StationLocation.objects.create(
            id=3, name="Station A", latitude=13.736717, longitude=100.523186
        )
        self.station_d = StationLocation.objects.create(
            id=4, name="Station B", latitude=13.738000, longitude=100.524000
        )
        self.station_e = StationLocation.objects.create(
            id=5, name="Station A", latitude=13.736717, longitude=100.523186
        )
        self.station_f = StationLocation.objects.create(
            id=6, name="Station B", latitude=13.738000, longitude=100.524000
        )
        self.station_h = StationLocation.objects.create(
            id=7, name="Station A", latitude=13.736717, longitude=100.523186
        )
        self.station_i = StationLocation.objects.create(
            id=8, name="Station B", latitude=13.738000, longitude=100.524000
        )

        # Create two recent feedbacks
        Feedback.objects.create(bus_id=1, bus_line="A1", bus_stop="Stop1", passenger_density=4, comment="Crowded")
        Feedback.objects.create(bus_id=1, bus_line="A1", bus_stop="Stop2", passenger_density=2, comment="Chill")

        LineOneRoute.objects.create(station=self.station_a, order=1)
        LineOneRoute.objects.create(station=self.station_b, order=2)
        LineThreeRoute.objects.create(station=self.station_c, order=1)
        LineThreeRoute.objects.create(station=self.station_d, order=2)
        LineFiveRoute.objects.create(station=self.station_f, order=1)
        LineFiveRoute.objects.create(station=self.station_e, order=2)
        LineSpecialRoute.objects.create(station=self.station_h, order=1)
        LineSpecialRoute.objects.create(station=self.station_i, order=2)
