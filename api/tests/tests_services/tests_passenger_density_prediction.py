from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from api.models import Feedback
from api.services.passenger_density_prediction_service import passenger_density_prediction

from unittest import skip

class PassengerDensityPredictionTest(TestCase):

    def test_prediction_with_recent_feedbacks(self):
        # Ensure the function returns the average
        result = passenger_density_prediction(bus_id=1)
        self.assertEqual(result, 3.0)

    def test_prediction_with_no_recent_feedbacks(self):
        # Create old feedback (e.g., 2 hours ago)
        Feedback.objects.create(
            bus_id=1,
            bus_line="A1",
            bus_stop="Stop1",
            passenger_density=5,
            comment="Old",
        )
        Feedback.objects.filter().update(timestamp=timezone.now() - timedelta(hours=2))

        # Should return the default value (3)
        result = passenger_density_prediction(bus_id=1)
        self.assertEqual(result, 3)
