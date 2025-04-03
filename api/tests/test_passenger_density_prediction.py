import unittest

from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from api.models import Feedback
from api.services import passenger_density_prediction

class PassengerDensityPredictionTest(TestCase):

    def test_prediction_with_recent_feedbacks(self):
        # Ensure the function returns the average
        result = passenger_density_prediction(bus_id=1)
        self.assertEqual(result, 3.0)

    def test_prediction_with_no_recent_feedbacks(self):
        Feedback.objects.filter().update(timestamp=timezone.now() - timedelta(hours=2))

        # Should return the default value (3)
        result = passenger_density_prediction(bus_id=1)
        self.assertEqual(result, 3)
