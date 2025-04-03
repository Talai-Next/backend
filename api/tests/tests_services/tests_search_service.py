from api.models import StationLocation, LineOneRoute
from api.services.search_service import (
    find_nearest_station,
    find_available_line,
    find_bus_route,
    find_nearest_accessible_station,
)
from api.tests.tests_base import BaseTest


class SearchServiceTest(BaseTest):

    def test_find_nearest_station(self):
        result = find_nearest_station(13.737000, 100.523500)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Station A")

    def test_find_available_line(self):
        result = find_available_line(self.station_a.id)
        self.assertIn("1", result)

    def test_find_bus_route(self):
        result = find_bus_route(self.station_a.id, self.station_b.id)
        self.assertEqual(result, "1")

    def test_find_nearest_accessible_station(self):
        result = find_nearest_accessible_station(
            self.station_a.latitude, self.station_a.longitude, self.station_b.id
        )
        self.assertEqual(result.name, "Station A")
