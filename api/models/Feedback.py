from django.db import models
from django.utils.timezone import now


class Feedback(models.Model):
    bus_id = models.CharField(null=True, max_length=10)
    bus_line = models.CharField(null=True, max_length=3)
    bus_stop = models.CharField(null=True, max_length=10)
    passenger_density = models.IntegerField(
        verbose_name="Passenger Density",
        choices=[
            (1, "Very Low"),
            (2, "Low"),
            (3, "Medium"),
            (4, "High"),
            (5, "Very High"),
        ],
    )
    comment = models.CharField(max_length=255, verbose_name="Obstacle Type")
    timestamp = models.DateTimeField(default=now)
