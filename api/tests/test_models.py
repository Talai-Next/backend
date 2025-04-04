from api.tests.test_base import BaseTest
from api.models import (
    Feedback, LineFiveRoute, LineOneRoute, LineThreeRoute,
    LineSpecialRoute, ObstacleType, ObstaclePosition, StationLocation
)

class FeedbackModelTest(BaseTest):
    def test_feedback_creation(self):
        feedback = Feedback.objects.create(
            bus_id=2,
            bus_line="B2",
            bus_stop="Stop3",
            passenger_density=3,
            comment="Normal",
        )
        self.assertEqual(feedback.bus_id, 2)
        self.assertEqual(feedback.bus_line, "B2")
        self.assertEqual(feedback.bus_stop, "Stop3")
        self.assertEqual(feedback.passenger_density, 3)
        self.assertEqual(feedback.comment, "Normal")

    def test_passenger_density_choices(self):
        choices = dict(Feedback._meta.get_field('passenger_density').choices)
        self.assertIn(1, choices)
        self.assertEqual(choices[1], "Very Low")
        self.assertEqual(choices[5], "Very High")


class LineRouteModelTest(BaseTest):
    def test_line_one_route_creation(self):
        route = LineOneRoute.objects.create(station=self.station_a, order=99)
        self.assertEqual(route.order, 99)
        self.assertEqual(route.station, self.station_a)

    def test_line_three_route_creation(self):
        route = LineThreeRoute.objects.create(station=self.station_c, order=88)
        self.assertEqual(route.order, 88)
        self.assertEqual(route.station, self.station_c)

    def test_line_five_route_creation(self):
        route = LineFiveRoute.objects.create(station=self.station_f, order=77)
        self.assertEqual(route.order, 77)
        self.assertEqual(route.station, self.station_f)

    def test_line_special_route_creation(self):
        route = LineSpecialRoute.objects.create(station=self.station_h, order=66)
        self.assertEqual(route.order, 66)
        self.assertEqual(route.station, self.station_h)


class ObstacleTypeModelTest(BaseTest):
    def test_obstacle_type_creation(self):
        obstacle_type = ObstacleType.objects.create(name="Construction")
        self.assertEqual(obstacle_type.name, "Construction")
        self.assertEqual(str(obstacle_type), "Construction")


class ObstaclePositionModelTest(BaseTest):
    def test_obstacle_position_creation(self):
        obstacle_type = ObstacleType.objects.create(name="Tree")
        position = ObstaclePosition.objects.create(
            latitude=13.75,
            longitude=100.51,
            obstacle_type=obstacle_type
        )
        self.assertEqual(position.latitude, 13.75)
        self.assertEqual(position.longitude, 100.51)
        self.assertEqual(position.obstacle_type, obstacle_type)


class StationLocationModelTest(BaseTest):
    def test_station_location_creation(self):
        station = StationLocation.objects.create(
            station_code="ENG1",
            name="Engineering Building 1",
            name_eng="ENG Building 1",
            latitude=13.736,
            longitude=100.523
        )
        self.assertEqual(station.station_code, "ENG1")
        self.assertEqual(station.name, "Engineering Building 1")
        self.assertEqual(station.name_eng, "ENG Building 1")
        self.assertEqual(station.latitude, 13.736)
        self.assertEqual(station.longitude, 100.523)
